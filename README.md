# AI_Grader2024

## Framework 

本仓库为AI 自动批改项目的基础框架，提供了基本的结构化数据读取、逐题目批改以及批改结果报告生成的功能，可以选择在此框架上进行扩展。

### 项目结构

项目根目录下包含以下模块：
- `data/`: 用于存放输入输出数据，其中包含`1/`作为第一次作业的示例数据，其下为: 
  - `raw/`: 用于存放学生的原始提交结构化数据，每个文件以学生学号命名（匿名化后），为Json格式，其中具体结构见后流程部分介绍
  - `refs/`: 用于存放标准答案的结构化数据，每次作业有唯一的标准答案，为Json格式，内容见后
  - `results/`: 用于存放批改结果，每份作业会同时生成Json和Md格式的批改结果，分别用于后续统计和直观展示
- `instance/`: 定义了项目中使用的数个示例类型:
  - `problem.py`: 定义了学生作业类`StudentPA`及其内部类型，逻辑见后
  - `ref_problem.py`: 定义了标准答案类`RefPA`及其内部类型，逻辑见后
- `checker/`: 包含了核心的批改逻辑，其中:
  - `base.py`: 定义批改基类`BaseChecker` 
  - `example_checker.py`: 一个简单的示例批改器
- `reporter/`: 包含了批改结果报告生成逻辑，其中:
  - `default_reporter.py`: 定义默认的报告生成器
  - `aggregator.py`: 用于在Md报告中生成整份作业的统计信息
- `utils/`: 包含了项目中使用的一些工具函数
  - `apis/`: 提供了简单串行调用OpenAI like API和Dify App API的接口
  - `wrappers/`: 放置每个API调用格式的外部封装，包括请求的System prompt、User query format等

根目录下`README_legacy.md`提供了旧版本的README，包含了项目的历史信息，以及安装和运行示例。

### 基本流程

下面介绍框架的基本流程

#### 数据读取

每次作业的数据包含“作业”，“题目”，“子题目”三个层次，其中子题目可能具有多个层次，但是我们为了简单将其展平为单层，多层的题号使用“@”符连接，例如“1)@a)”表示1)下的a)子题目。

标准答案的输入数据示例如下：
```json
{
    //... some problems
    "1.2": {
        "problem": "$6$个男生和$5$个女生围在一圆桌旁，若\n%\n\begin{enumerate}[label={\rm (arabic*)}]\n    item 任何两个女生不相邻；\n    item 所有女生形成一个整体；\n    item 女生$A$两侧均是男生。\nend{enumerate}\n%\n分别讨论有多少种方案。",
        "answers": {
            "(1)": [
                {
                    "answer": "$6$个男生之间形成$6$个空位，$5$位女生每人占据一个空位。从剩下的那个空位处切开圆排列、顺时针展开，即得到男女间隔的一个线排列，而所求的圆排列显然和展开后的线排列一一对应。因此，方案数即为$6! \\dotp 5! = 86400$",
                    "rules": [
                        {
                            "rule": "女生和男生交错排列",
                            "score": 1
                        },
                        {
                            "rule": "转化为线排列",
                            "score": 1
                        },
                        {
                            "rule": "答案正确",
                            "score": 1
                        }
                    ]
                }
            ],
            "(2)": [
                {
                    "answer": "将全体女生视作一个$6!$种可能性的整体与$5$个男生作圆排列，方案数即为$6! \\dotp 5! = 86400$；",
                    "rules": [
                        {
                            "rule": "将女生视为一个整体",
                            "score": 1
                        },
                        {
                            "rule": "女生内部排列",
                            "score": 1
                        },
                        {
                            "rule": "整体做圆排列",
                            "score": 1
                        },
                        {
                            "rule": "答案正确",
                            "score": 1
                        }
                    ]
                }
            ],
            // ... some other subproblems
        }
    },
    //... some other problems
}
```
- 整个Dict对应于一次PA的参考答案，其中key对应每个题目的题号，value为题目的描述和答案:
- 每个题目的Dict中:
  - `problem`: 为整个题目的描述，包含题目的描述和子题目的描述。这里由于并不容易处理小题之间的相互依赖以及题干共用的问题，所以我们仅将每个子题目的解答拆分开来，而题目的描述保持完整。
  - `answers`: 为每个子题目的参考答案，Dict中的key为子题目的题号，value为这个子题目的可能解题方案的列表
- 每个子题目的List中，每个Dict对应于这个子题目一种可能的求解流程，比如可以用代入规则、命题演算、真值表等方法求解同一个表达式的真值，它们属于并列的解题方法。每个Dict中:
  - `answer`: 这一种解题方法的标准答案，文本格式
  - `rules`: 这一种解题方法的评分标准，List中每个Dict对应于一条评分规则，其中包含评分规则的描述`rule`和分值`score`，作为AI的输入

`ref_problem.py`中`RefPA`课通过`from_json`方法直接读取一个标准答案的Json文件，生成一个`RefPA`对象。每个题目对应于一个`RefProblem`对象，其中包含了题目的描述和子题目的参考答案。每个子题目对应于一个`BaseProblem`对象，其中包含了子题目的题号和解题方法列表。每个解题方法对应于一个`Solution`对象，其中包含了答案和评分规则。

学生答案的输入数据示例如下：
```json
{
    // ... some problems
    "1.2": {
        "(1)": "$6$个男生之间形成$6$个空位，$5$位女生每人占据一个空位。从剩下的那个空位处切开圆排列、顺时针展开，即得到男女间隔的一个线排列，而所求的圆排列显然和展开后的线排列一一对应。因此，方案数即为$6! \\dotp 5! = 86400$",
        "(2)": "将全体女生视作一个$6!$种可能性的整体与$5$个男生作圆排列，方案数即为$6! \\dotp 5! = 86400$；",
        "(3)": "从$8$个男生中依次挑选两人放置在$A$的左右两侧（$P(6, 2)$种方案），然后将其视作一个整体与其余$8$个学生作圆排列，方案数即为$P(6, 2) \\dotp 8! = 1\\,209\\,600$"
    },
    // ... some other problems
}
```
- 顶层为Dict，key为题目的题号，value为学生的答案
- 每个题目的Dict中，key为子题目的题号，value为学生的答案文本

`problem.py`中`StudentPA`通过`load_raw`方法直接读取一个学生答案的Json文件，生成一个`StudentPA`对象。每个题目对应于一个`StudentProblem`对象，其中包含了题目的描述和子题目的学生答案。每个子题目对应于一个`StudentProblem`对象，其中包含了子题目的题号和学生答案。

经过批改之后，将会将批改相关信息写入对应的`StudentPA`对象中，包括得分、匹配到的解题方法、是否出现异常等信息，通过`to_dict`导出为Json格式的批改结果。`load_graded`方法可以加载一个批改结果的Json文件，生成一个包含批改结果的`StudentPA`对象。

#### 批改逻辑

基础框架通过逐一检查参考答案中给定的评分规则进行批改，见`example_checker.py`中的`check`方法:

```python
def check(self, ref_pa, student_pa):
        from tqdm import tqdm

        for problem_id, ref_problem in tqdm(ref_pa.problems.items(), desc="Checking problems", total=len(ref_pa.problems)):
            student_problem = student_pa.problems[problem_id]
            
            for subproblem_id, ref_subproblem in tqdm(ref_problem.answers.items(), desc="Checking subproblems", total=len(ref_problem.answers)):
                student_solution = student_problem.answers[subproblem_id]
                
                # TODO: add solution matching logic here
                solution_id = 0
                ref_solution = ref_subproblem.solutions[solution_id]
                student_solution.set_solution(ref_solution.answer, solution_id)

                # check rule by rule
                for id, rule in tqdm(enumerate(ref_solution.rules), desc="Checking rules", total=len(ref_solution.rules)):
                    inputs = format_openai_inputs(
                        ref_problem.problem,
                        ref_solution,
                        student_solution,
                        id,
                    )
                    response = openai_completion(**inputs)

                    process, score = self.parse_grading_response(response)
                    
                    tqdm.write(f"Process: {process}")
                    tqdm.write(f"Score: {score}")
                    if not rule.check_valid_score(score):
                        student_solution.set_error(f"Invalid score {score} for rule {rule.rule} (max {rule.score})")

                    student_solution.add_score(rule, process, score)
                
                student_solution.finalize(ref_solution.rules)

        return student_pa
```
- 基础框架并没有实现匹配解题方法的逻辑，暂时直接使用首个解题方法进行批改。后续可加入根据参考答案文本和学生答案首先匹配解题方法，再进行批改，并在无匹配时标记新解题方法异常。

#### 报告生成

`default_reporter.py`中的`generate_reports`方法用于生成批改结果的报告，其中包含了每个题目的批改结果和整份作业的统计信息。以包含批改结果的`StudentPA`对象为输入，会在指定的Json和Md文件路径下生成对应的报告。

对于出现异常的题目，在报告中会被标记为`N/A`，并不会参与统计分数的计算。后续可以加入对应异常信息的统计。