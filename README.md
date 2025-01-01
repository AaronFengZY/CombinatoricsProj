# AI_Grader2024

## 简介

本项目旨在为编程作业或数学推导题提供自动批改、报告生成以及检索增强 (RAG) 的辅助工具。通过对参考答案与学生答案进行对比分析，实现对解题方法与评分规则的自动评估，并最终生成 Markdown 或 JSON 格式的批改报告。项目还提供了自动化测评脚本，便于对批改结果进行量化评估。

---

## 项目结构

本项目包含以下主要目录及文件：

- `data/`: 用于存放输入输出数据，包括章节测试样本、处理脚本以及测试样本配置文件等。常见结构示例：
  ```
  data/
  ├── 0X
  ├── 1
  ├── 1B
  ├── 1A
  └── ...
  ```
  - `hw_base_student_config.json`: 指定测试样本路径及其他配置信息  
  - `add_to_json.py` / `process.py`: 数据预处理或后处理脚本  
  - 以数字或字母开头的文件夹中通常存放对应章节或作业号下的原始/参考/生成的作业数据

- `instance/`: 定义了项目中使用的若干示例类型  
  - `problem.py`: 定义了学生作业类 `StudentPA` 及其内部类型，提供从原始 JSON 读取学生答案的功能  
  - `ref_problem.py`: 定义了标准答案类 `RefPA` 及其内部类型，提供从 JSON 加载参考答案的功能

- `DocToolbox/`: （原先的 `checker/` 文件夹现已更名为 `DocToolbox/`）包含核心的批改逻辑及文档检索逻辑
  - `checker.py`: 主要核心逻辑所在，定义 `Checker` 类及其 `check` 方法，内部实现批改流程  
  - `base.py`: 批改基类 `BaseChecker`  
  - `PDFRetriever.py`: 用于实现 RAG（Retrieval-Augmented Generation）相关检索逻辑，例如从 PDF 中检索题目信息或答案线索  
  - `__init__.py`: Python 包初始化文件

- `reporter/`: 用于生成批改结果的报告
  - `default_reporter.py`: 默认的报告生成器，可生成 Markdown 与 JSON 格式的结果  
  - `aggregator.py`: 在报告中统计整份作业的概览、汇总信息

- `utils/`: 存放项目中的工具函数或外部 API 封装等
  - `apis/`: 提供与外部 API（如 OpenAI 或 Dify App 等）串行调用的简单接口  
  - `wrappers/`: 对各类 API 的调用格式或 Prompt 进行封装

- `eval/`: 用于对最终批改结果进行测评
  - `eval.py`: 评估逻辑脚本，可根据已有的批改结果计算多种评估指标  
  - `eval.sh`: 运行测评的 Bash 脚本，可一次性批量评估多个作业/学生的结果，并生成测评报告

- `checker.py`: 可以直接调用的批改脚本（示例实现同 `DocToolbox/checker.py` 相似，但可根据需求单独执行）

- `checker.sh`: Bash 脚本，用于批量对指定作业/学生进行批改，脚本内容示例如下：
  ```bash
  #!/bin/bash

  # Define hw_base and its associated student_ids as a mapping
  declare -A hw_base_students

  hw_base_students["data/1"]="1"
  hw_base_students["data/0X"]="Ch0-0X-10 Ch0-0X-12"
  hw_base_students["data/1B"]="Ch1-1B-13 Ch1-1B-2 Ch1-1B-4 Ch1-1B-6 Ch1-1B-7"
  hw_base_students["data/2A"]="Ch2-2A-1 Ch2-2A-10 Ch2-2A-2 Ch2-2A-4 Ch2-2A-6 Ch2-2A-7 Ch2-2A-9"
  hw_base_students["data/2X"]="Ch2-2X-14 Ch2-2X-7 Ch2-2X-8 Ch2-2X-9"
  hw_base_students["data/1X"]="Ch1-1X-10 Ch1-1X-12 Ch1-1X-13 Ch1-1X-14 Ch1-1X-2 Ch1-1X-5 Ch1-1X-7"
  hw_base_students["data/1A"]="Ch1-1A-1 Ch1-1A-10 Ch1-1A-11 Ch1-1A-13 Ch1-1A-14 Ch1-1A-15 Ch1-1A-16 Ch1-1A-17 Ch1-1A-18 Ch1-1A-20 Ch1-1A-21 Ch1-1A-22 Ch1-1A-24 Ch1-1A-25 Ch1-1A-3 Ch1-1A-4 Ch1-1A-5 Ch1-1A-6 Ch1-1A-8 Ch1-1A-9"
  hw_base_students["data/2B"]="Ch2-2B-1 Ch2-2B-2"
  hw_base_students["data/6X"]="Ch6-X-1 Ch6-X-2 Ch6-X-3 Ch6-X-4 Ch6-X-5"
  hw_base_students["data/4X"]="Ch4-X-10 Ch4-X-6 Ch4-X-7 Ch4-X-9"
  hw_base_students["data/3X"]="Ch3-3X-10 Ch3-3X-11 Ch3-3X-12 Ch3-3X-6 Ch3-3X-7"

  # Set the number of responses as a default parameter
  num_responses=1

  # Iterate over the mapping and run the checker for each hw_base and student_id
  for hw_base in "${!hw_base_students[@]}"; do
      student_ids=${hw_base_students[$hw_base]}
      for student_id in $student_ids; do
          python3 checker.py --hw_base="$hw_base" --num_responses="$num_responses" "$student_id"
      done
  done
  ```

- `requirements.txt`: 用于记录依赖库，可通过 `pip install -r requirements.txt` 安装项目所需的第三方库。

---

## 环境配置

如果安装了 [conda](https://docs.conda.io/en/latest/)，可在项目根目录下执行以下命令来创建并激活 Python 3.9 的环境（此处以环境名 `combinatorics` 为例）：

```bash
conda create --name combinatorics python=3.9
conda activate combinatorics
```

然后安装项目依赖：
```bash
pip install -r requirements.txt
```

完成以上步骤后，即可开始使用本项目提供的脚本和工具。

---

## 基本批改流程

### 1. 数据读取

项目将作业数据分为“作业”、“题目”、“子题目”三个层次；子题目若有多层，本框架会以“@”连接多层子题号。如：  
- **标准答案**（`ref_problem.py` 的 `RefPA` 可使用 `from_json` 方法读取）  
- **学生答案**（`problem.py` 的 `StudentPA` 可使用 `load_raw` 方法读取）

### 2. 批改逻辑

主要位于 `DocToolbox/checker.py` 中 `Checker` 类的 `check` 方法，可根据子题目的不同解法规则进行评分。示例逻辑：
```python
def check(self, ref_pa, student_pa):
    # 遍历题目
    for problem_id, ref_problem in ref_pa.problems.items():
        student_problem = student_pa.problems[problem_id]
        
        # 遍历子题目
        for subproblem_id, ref_subproblem in ref_problem.answers.items():
            student_solution = student_problem.answers[subproblem_id]
            
            # (可扩展) 选取最佳解法、逐条评分
            ref_solution = ref_subproblem.solutions[0]
            student_solution.set_solution(ref_solution.answer, 0)

            for rule_id, rule in enumerate(ref_solution.rules):
                # 简单示例：若学生答案包含某关键词则给分
                if rule.rule in student_solution.text:
                    score = rule.score
                else:
                    score = 0
                student_solution.add_score(rule, "批改说明", score)

            # 统计并计算最终得分
            student_solution.finalize(ref_solution.rules)

    return student_pa
```

### 3. 报告生成

批改完成后，可调用 `reporter/default_reporter.py` 的 `generate_reports` 方法生成 Markdown 和 JSON 格式结果文件：
- JSON 文件包含每个子题的评分、匹配的解题方法与规则等信息  
- Markdown 文件包含分数、整体统计，以及异常情况等说明，便于快速查看

---

## 批改结果测评

项目中提供了 `eval/` 文件夹下的测评脚本，用于对已完成批改的结果进行量化评估：

- `eval.py`: 评估脚本，核心测评指标包括：

  1. **ACC** (Accuracy-like metric)  
     \[
     \mathrm{ACC} = 1 - \sum_{l=1}^{\text{subproblem}} \sum_{j=1}^{\text{rule}} \frac{|s_{\mathrm{gt}} - s_{\mathrm{llm}}|}{s_{\mathrm{total}}}
     \]
     其中 \( s_{\mathrm{gt}} \) 表示该子题的真值分数，\( s_{\mathrm{llm}} \) 表示模型打分结果，\( s_{\mathrm{total}} \) 为可用的总分，根据所有子题、规则进行归一化处理。

  2. **Average Absolute Error (AAE)**:  
     \[
     \text{AAE} = \frac{\sum |s_{\mathrm{gt}} - s_{\mathrm{llm}}|}{\text{总题数}}
     \]
     即所有学生在所有子题的绝对误差平均值。

- `eval.sh`: Bash 脚本，一次性批量评估多个作业/学生，最终评估结果会输出在控制台，并同时以 JSON 和 Markdown 格式分别保存在 `result/` 文件夹中。  
  示例运行命令：
  ```bash
  bash ./eval/eval.sh
  ```

### 测评示例

假设我们对 `data/0X` 下的作业进行测评，运行：
```bash
bash ./eval/eval.sh
```
输出示例可能如下：
```
=== Now evaluating assignment 'data/0X' with students: Ch0-0X-10 Ch0-0X-12

Evaluating assignment in: /home/v-zhifeng/HPE/CombinatoricsProj/data/0X
Students: ['Ch0-0X-10', 'Ch0-0X-12']

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
该结果同时以 JSON 和 Markdown 文件的形式保存在 `result/0X/` 文件夹中，便于后续检阅和分析。

---

## 使用示例

1. **批改（单次运行 Python 脚本）：**
   ```bash
   python3 checker.py --hw_base="data/1" --num_responses=1 "1"
   ```
   此命令会根据 `data/1` 目录和作业编号 `1` 来进行批改，生成对应的 Markdown 和 JSON 报告。

2. **批改（批量运行 Bash 脚本）：**
   ```bash
   bash checker.sh
   ```
   此命令会批量遍历脚本中配置的 `hw_base` 与 `student_ids`，分别执行批改流程，并在对应目录下生成报告。

3. **测评（批量评估）：**
   ```bash
   bash ./eval/eval.sh
   ```
   此命令会批量遍历配置好的作业路径与学生 ID，计算 ACC、AAE 等测评指标，并将结果保存到 `result/` 文件夹中。

---

## 其他说明

- **异常处理**  
  若在批改过程中无法匹配参考解法或发现异常情况，可在最终结果中标记为 `N/A`，并在报告中体现。

- **RAG（Retrieval-Augmented Generation）**  
  `DocToolbox/PDFRetriever.py` 可扩展实现基于检索的增强生成逻辑，从 PDF 或其他文档中获取题干或答案线索，与大模型配合进行答案比对。

- **后续扩展**  
  可扩展更智能的解题匹配、细化评分标准或复杂的上下文管理逻辑，提升批改准确度和多场景适用性。

如有任何疑问或改进建议，欢迎在 Issue 中讨论或提交 PR。祝学习/使用愉快！