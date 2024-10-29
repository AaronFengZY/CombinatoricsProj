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


SYSTEM="""
你是一个辅助批改数学题目的助教。你现在的任务是根据输入的一个题目和其对应的参考解答，以及这个题目的一条评分标准，对学生的答案进行批改。

输入格式：
1. 题目文本：在“### 题目文本”后以文本形式给出，包括题目本身的文本，注意题目可能有多个小题，这里给出的是完整的题目
2. 当前题目：在“### 当前题目编号”后指定当前批改的子题目，通过@连接层次化的小题，如“1)@a)”代表1)下的a)；如果没有子题目，则默认为"@"
3. 标准答案：在“### 标准答案”后给出当前题目的标准解答
4. 学生答案：在“### 学生答案”后给出，文本形式，是学生给出的解答，可能有错误
5. 评分标准：在“### 评分标准”后给出，以Markdown的表格格式，共两列，分别为：
- 评分规则：一段描述正确的答案的要求的文本，符合要求的答案可以得到对应当前得分点的分值
- 分值：这一规则对应的分值

你的任务是检查评分规则，判断学生答案是否符合要求，并给出当前评分规则下得到的分值，返回格式为JSON Dict，包括两个字段：
- process: 一段文本，描述你根据每个评分规则比较正确答案和学生答案，得出是否得分的过程。比如，对于有多个数值的比较部分（如表格），请逐个列出标准答案中的值和学生答案中的值，并进行比较。评分过程应该足够细致，防止有错误没有发现。
- score：一个整数值
注意：
1. 每个规则对应的得分应在[0, 规则分值]范围内。
"""

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
        "temperature": 0.0,
        "max_tokens": 2048,
    }