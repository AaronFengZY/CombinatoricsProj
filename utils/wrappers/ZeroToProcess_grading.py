"""
    Wrapper for the example grading API
"""
from instance.ref_problem import Solution
from instance.problem import StudentSolution

ORIGINAL_SYSTEM_PROMPT = """你是一名勤勉而谨慎的数学批改助教。你的职责是根据以下信息，对学生的解答进行评分，并提供评语和最终得分。

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

RECHECK_ADDENDUM = """\
在本题的第一次批改中，评分结果为 0 分。请你再次仔细审阅，看看是否存在任何被忽视的部分正确思路或步骤。
如果确有部分正确之处，请在 [0, 该规则分值] 范围内给出适当的分值，并在 "process" 中说明理由。
如果确认仍为 0 分，也请在 "process" 中说明原因。
请继续保持仅输出 JSON 格式，并遵守以上评分要求。
"""

SYSTEM_PROMPT_RECHECK = ORIGINAL_SYSTEM_PROMPT + "\n\n" + RECHECK_ADDENDUM

# ZERO_SCORE_CHECK_PATTERN = """
# 我们在第一次批改中得出的结论是本题总分为 0。
# 现在请再次审阅学生答案，看看是否存在任何可能被忽视的部分正确之处。
# 如果确有部分正确之处，请在 [0, {max_score}] 范围内给出一个新的分值，并在 "process" 中详细说明理由。
# 如果确认仍然是 0 分，请说明缺少哪些核心要点导致无法得分。
# 输出必须是纯 JSON，对应两个字段：
# 1. "process"：说明再次审阅的判断依据。
# 2. "score"：在 [0, {max_score}] 区间内的整数得分。
# 注意：禁止输出除上述 JSON 以外的任何内容。
# """


def format_single_rule_zero_score_recheck_inputs(
    problem: str,
    subproblem_id: str,
    reference_answer: str,
    student_answer: str,
    single_rule,
):
    """
    Build a prompt for rechecking a single rule that was initially scored 0.
    We reuse the same system instructions but add a note that we are re-checking
    only this rule to see if partial correctness was missed.
    """

    # Convert the single rule to Markdown
    single_rule_md = single_rule.format_md_table()

    user_prompt = f"""
### 题目文本
{problem}

### 当前题目编号
{subproblem_id}

### 标准答案
{reference_answer}

### 学生答案
{student_answer}

### 需要复查的评分标准
{single_rule_md}

我们在之前的批改中对这个评分规则打了 0 分。请再次细致对比学生答案和标准答案，判断是否存在任何遗漏的部分正确性。如果确有部分正确，请给出 [0, {single_rule.score}] 范围内的适当整数分值并在 "process" 字段中说明理由；若仍为 0 分，也请说明原因。

仅输出以下 JSON 字段：
1. "process": 说明重新审阅的判定依据
2. "score": 在 [0, {single_rule.score}] 范围内的整数得分
"""

    # Either reuse your original system prompt or a modified "recheck" system prompt
    # For example:

    return {
        "model": "deepseek-chat",
        "system_prompt": SYSTEM_PROMPT_RECHECK,  # A variation or the same prompt with a recheck note
        "user_prompt": user_prompt,
        "history": [],
        "temperature": 0.0,
        "max_tokens": 2048,
    }