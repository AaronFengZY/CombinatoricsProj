下面是一份示例性的“实验报告”升级版本，基于你提供的 **AI_Grader2024** 项目整体结构、功能说明和测评工具，融入了之前的自动批改框架与评测指标等内容。可根据实际需求对细节进行增减、调整。

---

# 实验报告：基于 Deepseek API 的自动作业批改与评测框架研究

**实验人**：冯志远、燕山楠

---

## 一、引言

在教育信息化的浪潮下，如何利用大规模预训练语言模型（LLM）来为编程类和数学推导类题目进行自动批改，一直是在线教育平台和教学辅助系统的重要课题。本实验项目 (**AI_Grader2024**) 的目标在于：  
1. **构建可扩展的自动批改框架**：对学生答案进行结构化解析，结合 RAG（Retrieval-Augmented Generation）技术，实现对标准答案与学生答案的对比分析。  
2. **设计合理的多维度评分与报告输出机制**：同时支持 JSON、Markdown 等多种格式，对各子题目进行分项打分并汇总。  
3. **提供系统化的测评工具**：通过测评指标（Accuracy-like metric、平均绝对误差等）量化自动评分的质量，并对批改结果进行整体分析。

本实验结合了 Deepseek API 提供的对话式大模型能力与自行构建的向量检索数据库，对“组合数学”相关题目及编程作业进行自动打分与评测，对比人工评分来验证系统的有效性。

---

## 二、项目总体结构与功能

### 2.1 项目结构概览

项目的整体目录组织如下：

- **`data/`**：用于存放输入输出数据，包括章节测试样本、处理脚本以及测试样本配置文件等。  
  - 存放各章节、各作业号对应的原始题目信息与学生答案文件。  
  - 例如：`data/0X/`, `data/1B/` 等。  
  - 常见配置文件：`hw_base_student_config.json`、`add_to_json.py`、`process.py` 等。

- **`instance/`**：定义用于加载、存储与管理题目和答案的核心数据结构。  
  - `problem.py`：学生答案类 `StudentPA`；  
  - `ref_problem.py`：标准答案类 `RefPA`。

- **`DocToolbox/`**：（原先命名为 `checker/`）包含主要的批改逻辑与文档检索逻辑。  
  - `checker.py`：`Checker` 类及其 `check` 方法，是批改流程的核心；  
  - `base.py`：提供批改基类 `BaseChecker`；  
  - `PDFRetriever.py`：可实现 RAG（如从 PDF 中检索相关题目信息或答案线索），辅助大模型回答。

- **`reporter/`**：报告生成模块  
  - `default_reporter.py`：默认报告生成器，输出 Markdown 或 JSON 格式。  
  - `aggregator.py`：收集整份作业的整体打分与错误统计信息。

- **`utils/`**：辅助工具、函数或外部 API 封装  
  - `apis/`：与 OpenAI / Dify App 等 API 的调用接口；  
  - `wrappers/`：对 Prompt 或调用参数等进行二次封装。

- **`eval/`**：用于最终测评  
  - `eval.py`：核心评估指标脚本；  
  - `eval.sh`：批量评估多个作业或学生作业，生成评测报告。

- **`checker.py`**：可直接执行的批改脚本（独立于 `DocToolbox/checker.py` ），也可用 `checker.sh` 调用。

- **`checker.sh`**：Bash 脚本，用于批量自动批改指定作业/学生的答案，遍历配置并调用 Python 脚本执行。

- **`requirements.txt`**：项目依赖列表。

通过以上结构，项目分别覆盖了数据管理、批改核心逻辑、检索增强、报告输出以及批改结果测评的全流程。

---

## 三、自动批改的核心逻辑与实现

### 3.1 数据读取与分层

**AI_Grader2024** 将作业划分为“作业 (hw) — 题目 (problem) — 子题 (subproblem)” 三级结构；其中子题可以进一步细分，如以 “@” 形式区分子子题。常用示例：  
- **标准答案**：由 `RefPA` 类统一管理和加载，支持多种解法的存储；  
- **学生答案**：通过 `StudentPA` 类从 JSON 文件读取，内部可映射到题目与子题的结构。

### 3.2 RAG 检索增强

为提高批改对题目背景与知识点的匹配度，我们在 `DocToolbox/PDFRetriever.py` 中实现了检索模块，主要流程如下：

1. 对相关文献（如《组合数学》PDF）进行文本拆分、向量化，并存入向量数据库；  
2. 当执行批改时，根据当前题目文本或题干，在数据库中检索相似度最高的若干（通常是 4 条）段落；  
3. 将这些段落与题目的 Prompt 合并输入 Deepseek API，让大模型在打分前能参考更多上下文。

通过此方式，可在自动评分中更准确地对学生答案是否符合对应知识点进行判断。

### 3.3 批改流程与两阶段打分

本项目在批改时还结合了 **两阶段打分** 的思路：

1. **第一阶段**：对每条打分规则严格判定；如若学生在所有规则下得分为 0，则进入第二阶段；  
2. **第二阶段**：重点审视学生在解题过程中是否有任何“部分正确”或“思路可取”之处，尽量减少误判导致的“全扣”情况。

在实现层面（示例性逻辑）：

```python
def check(self, ref_pa, student_pa):
    for problem_id, ref_problem in ref_pa.problems.items():
        student_problem = student_pa.problems[problem_id]
        
        for subproblem_id, ref_subproblem in ref_problem.answers.items():
            student_solution = student_problem.answers[subproblem_id]
            
            # 选取标准解
            ref_solution = ref_subproblem.solutions[0]
            
            # 第一阶段评分
            total_score = 0
            for rule_id, rule in enumerate(ref_solution.rules):
                # 若学生答案中包含指定关键词或满足判定条件则给分
                if rule.rule in student_solution.text:
                    score = rule.score
                else:
                    score = 0
                total_score += score
                student_solution.add_score(rule, "批改说明", score)
            
            # 如果第一阶段总分为 0，进行第二阶段再审阅
            if total_score == 0:
                # 进入再审阅逻辑...
                # 在此可调用特定 Prompt 让大模型“放宽”判定标准
                revised_score = self.recheck_process(student_solution, ref_solution)
                total_score = revised_score

            # 记录最终得分
            student_solution.finalize(ref_solution.rules)
    
    return student_pa
```

在 `recheck_process()` 里会有一个额外的 system_prompt 告知大模型这是第二轮检查，允许给部分分；从而避免一些细节上的“全错”漏判。

### 3.4 并行多响应与投票

在第一阶段评分时，如果需更高的稳健性，可进行“并行多响应”，即对同一个 Prompt 让大模型产生多个候选评分结果，再经由简单的投票机制选择出现次数最多的得分。若投票结果仍存在明显冲突，则引入人工裁决。示例代码片段（简化）：

```python
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    future_list = [
        executor.submit(openai_completion, **inputs) for _ in range(num_responses)
    ]
    
    attempts = []
    for future in concurrent.futures.as_completed(future_list):
        response = future.result()
        process, score = self.parse_grading_response(response)
        attempts.append((process, score))

# 对 attempts 中的 score 做频次统计，投票决定最终打分
```

---

## 四、测评指标与结果分析

### 4.1 测评指标

项目在 `eval/eval.py` 中实现了常用的两种测评指标，对自动批改结果进行量化评估：

1. **ACC (Accuracy-like metric)**  
   \[
   \mathrm{ACC} = 1 - \sum_{l=1}^{\text{subproblem}} \sum_{j=1}^{\text{rule}} \frac{|s_{\mathrm{gt}} - s_{\mathrm{llm}}|}{s_{\mathrm{total}}}
   \]  
   其中 \(s_{\mathrm{gt}}\) 为真值分数，\(s_{\mathrm{llm}}\) 为模型批改分数，\(s_{\mathrm{total}}\) 为单个子题（或整个卷面）的可用总分。

2. **平均绝对误差 (AAE)**  
   \[
   \mathrm{AAE} = \frac{\sum |s_{\mathrm{gt}} - s_{\mathrm{llm}}|}{\text{总子题数}}
   \]  
   衡量模型打分与人工打分在各子题上的平均偏离程度。

### 4.2 测试脚本与评测流程

- **`eval.sh`**：批量评测脚本，通过预先配置好的作业路径与学生 ID，一次性遍历并调用 `eval.py` 对已有的批改结果（JSON）进行统计。  
- 评测示例：
  ```bash
  bash ./eval/eval.sh
  ```
  输出示例（简化）：
  ```
  === Now evaluating assignment 'data/0X' with students: Ch0-0X-10 Ch0-0X-12
  
  --- Student: Ch0-0X-10 ---
    Ground Truth Score       : 9.5
    Final Graded Score       : 6.00
    Absolute Error           : 3.5000
    ACC                      : 0.6316
  
  --- Student: Ch0-0X-12 ---
    Ground Truth Score       : 9.5
    Final Graded Score       : 7.50
    Absolute Error           : 2.0000
    ACC                      : 0.7895
  
  === Overall Assignment Stats ===
  Mean ACC across 2 students       : 0.7105
  Mean Abs Error across 2 students : 2.7500
  ```

通过这类统计数据，我们能直观查看在不同作业、不同学生答案情况下，模型自动批改与人工评分的差距，以及两阶段打分与 RAG 技术对结果的影响。

---

## 五、实验结果与分析

> 以下为示例分析内容，可根据真实数据加以修改与补充。

1. **准确率与人工评分的比较**  
   - 经过测评脚本的统计，发现多数子题的自动评分与人工评分偏差在 ±5% ~ ±10% 之内，说明自动批改框架具有一定的可靠性。  
   - 对于少数需要极复杂背景知识或跨学科内容的题目，偏差明显增大，提示需要进一步扩充向量数据库。

2. **两阶段打分的效果**  
   - 约有 15% ~ 20% 的子题在第一阶段被判 0 分，其中有 40% ~ 50% 在第二阶段获得了部分分；  
   - 这种“再审阅”机制改善了全扣的极端情况，学生对系统的评价也较为正面，认为更贴近“人性化”评分。

3. **并行与投票机制**  
   - 在批量作业（如上百份）批改场景下，多线程并行处理缩短了整体完成时间达 30% ~ 50%；  
   - 一次生成多个候选评分后投票，有效减少了极端失误（如误判全对/全错），整体评分更加稳定；仅在 5% 左右的情况需要人工干预。

4. **RAG 技术贡献**  
   - 当检索到题目对应的核心知识点，模型判分更贴近人工结果；  
   - 若题目牵涉到数据库尚未收录的材料，则模型可能出现判断失误，需持续优化数据库内容与检索策略。

---

## 六、结论与展望

综上所述，本实验构建的 **AI_Grader2024** 框架在对组合数学与部分编程作业的自动批改上展现出了可行性与较好的一致性，通过两阶段打分与检索增强（RAG）的综合应用，使系统具备了较强的适应性和容错能力。同时，利用 `eval/` 目录下的测评脚本对批改结果进行 ACC 和 AAE 的量化分析，进一步验证了框架的可用性。

未来，我们计划：

1. **扩充知识库**：纳入更多学科（或更广泛的编程题）相关资料，让 RAG 在更多领域发挥作用；  
2. **细化评分规则**：在多学科、多题型场景下，进一步完善规则定义与打分逻辑，提高自动批改的精度与解释性；  
3. **人机协同迭代**：在实际教学中引入教师或助教的反馈数据，使自动批改系统持续迭代；  
4. **增强可移植性**：对接更多外部 API 或平台，如 Code Execution API、在线编程判题工具等，实现从语义批改到功能验证的扩展。

---

**实验人**：冯志远、燕山楠  

*本报告结合了自动批改框架的整体设计、RAG 技术、两阶段评分、并行投票等关键手段，同时展示了测评脚本及指标在量化评估自动批改性能方面的作用。希望该系统为自动化教学评估提供更多思路与参考。*