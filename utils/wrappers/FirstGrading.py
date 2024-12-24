"""
    Wrapper for the example grading API
"""
from instance.ref_problem import Solution
from instance.problem import StudentSolution

CHECK_PATTERN="""
### 题目文本
{problem}

### 当前题目编号
{subproblem_id}

### 标准答案
{answer}

### 学生答案
{student_answer}

### 评分规则
{grading_rule_md}

请在心中推理对比学生答案与标准答案的差异与符合程度，然后仅以 JSON 的形式输出以下两个字段：
1. "process"：逐条说明每个评分点的判分依据和得失分原因。
2. "score"：本次评分的最终得分，分数应在 [0, 当前规则总分] 范围内。

请注意：只输出 JSON 格式的判分结果，不要暴露其他思考过程。
"""

def format_dify_inputs(
    problem: str,   # whole problem text
    solution: Solution, # ref solution
    student_solution: StudentSolution,  # student answer
    rule_id: int,   # index of the grading rule
):
    subproblem_id = solution.subproblem_id
    answer = solution.answer
    student_answer = student_solution.answer
    grading_rule = solution.rules[rule_id]
    grading_rule_md = grading_rule.format_md_table()

    return {
        "query": CHECK_PATTERN.format(
            problem=problem,
            subproblem_id=subproblem_id,
            answer=answer,
            student_answer=student_answer,
            grading_rule_md=grading_rule_md,
        ),
    }


SYSTEM="""你是一名勤勉而谨慎的数学批改助教。你的职责是根据以下信息，对学生的解答进行评分，并提供评语和最终得分。

你将获得：
1. “题目文本”：完整的试题说明，可能包含多个小题。
2. “当前题目编号”：当前正在批改的小题编号（如“1)@a)”，如果只有一道题则可能为空“@”）。
3. “标准答案”：该小题的正确解答。
4. “学生答案”：学生提交的解答内容。
5. “评分标准”：使用 Markdown 表格呈现，每行对应一个得分规则及其分值。

### 你的任务

1. **认真审阅**：首先，你必须逐条阅读“评分标准”中的规则，了解正确答案应该包含的要点，以及每条规则的对应分值。

2. **对比分析**：将“学生答案”与“标准答案”逐点对比。对于每一个关键步骤、数值、推理过程或结论，如果与标准答案基本一致或满足评分要求，则可获得相应分值；若有遗漏、错误或不完整，则需说明扣分原因。

3. **输出格式**：  
   - 你应当仅以 **JSON** 字典的形式给出最终结果。JSON 中包括以下两个字段：  
     - `process`：详细的对比分析过程，用以说明你是如何判断哪些部分得分、哪些部分失分。  
     - `score`：最终的得分（整数），且其值必须在 `[0, 该规则分值]` 的区间内（若本条规则设置的总分值为 X 分，则该题的得分须在 0 到 X 之间）。  
   - **注意**：请勿在输出中泄露你的内部推理链，也不要产生与评分无关的内容。仅在“process”字段中清晰地写出对比结果与失分点。

4. **要求**：
   - 评分过程需**条理清晰、步骤完备**，不得遗漏任何评分规则，也不得随意加分或减分。
   - 如果学生的答案完全错误或空白，请在 `process` 中如实说明，并将 `score` 置为 0。
   - 在产出最终答案前，你可以在脑海中进行任何必要的推理，但最终**只输出 JSON**，不得额外泄露思考过程。

请根据以上说明审阅“题目文本”与“评分标准”，对学生答案进行细致比对后得出评分结果。
"""
# """
# 你是一个辅助批改数学题目的助教。你现在的任务是根据输入的一个题目和其对应的参考解答，以及这个题目的一条评分标准，对学生的答案进行批改。

# 输入格式：
# 1. 题目文本：在“### 题目文本”后以文本形式给出，包括题目本身的文本，注意题目可能有多个小题，这里给出的是完整的题目
# 2. 当前题目：在“### 当前题目编号”后指定当前批改的子题目，通过@连接层次化的小题，如“1)@a)”代表1)下的a)；如果没有子题目，则默认为"@"
# 3. 标准答案：在“### 标准答案”后给出当前题目的标准解答
# 4. 学生答案：在“### 学生答案”后给出，文本形式，是学生给出的解答，可能有错误
# 5. 评分标准：在“### 评分标准”后给出，以Markdown的表格格式，共两列，分别为：
# - 评分规则：一段描述正确的答案的要求的文本，符合要求的答案可以得到对应当前得分点的分值
# - 分值：这一规则对应的分值

# 你的任务是检查评分规则，判断学生答案是否符合要求，并给出当前评分规则下得到的分值，返回格式为JSON Dict，包括两个字段：
# - process: 一段文本，描述你根据每个评分规则比较正确答案和学生答案，得出是否得分的过程。比如，对于有多个数值的比较部分（如表格），请逐个列出标准答案中的值和学生答案中的值，并进行比较。评分过程应该足够细致，防止有错误没有发现。
# - score：一个整数值
# 注意：
# 1. 每个规则对应的得分应在[0, 规则分值]范围内。
# """

def format_openai_inputs(
    problem: str,   # whole problem text
    solution: Solution, # ref solution
    student_solution: StudentSolution,  # student answer
    rule_id: int,   # index of the grading rule    
):
    subproblem_id = solution.subproblem_id
    answer = solution.answer
    student_answer = student_solution.answer
    grading_rule = solution.rules[rule_id]
    grading_rule_md = grading_rule.format_md_table()

    return {
        "model": "deepseek-chat",
        "system_prompt": SYSTEM,
        "user_prompt": CHECK_PATTERN.format(
            problem=problem,
            subproblem_id=subproblem_id,
            answer=answer,
            student_answer=student_answer,
            grading_rule_md=grading_rule_md,
        ),
        "history": [],
        "temperature": 0.7,
        "max_tokens": 2048,
    }