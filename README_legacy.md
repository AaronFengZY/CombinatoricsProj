# llm-auto-grading
Framework for auto grading using LLMs.

## Log
- 2024/10/27: Initial Version
  - [x] Implement the basic structure of the framework.
    - [x] Example checker taking only the first solution for each subproblem
      - [ ] Add logic to go through all the solution of the given subproblem to match the student answer, or report a failure if no match is found.
    - [x] Default reporter to generate json and md report for each subproblem
      - [x] Add agg scores at the end of the report for each subproblem and each problem
      - [ ] Add ref scores to read TA's score for the student's solution and compare with the auto grading score
  - [x] Use openai api
  - [ ] Add parallel processing for speedup
  - [x] Add example ref for three problems and one example student pa
  - [ ] Finish full ref for all problems
  - [ ] Add more student data for examples
  - [ ] Implement simple frontend for TA to update the ref when a new solution is found or there is a bug in the ref
  - [ ] Implement a top-level instance to use the checker, check a batch of student submissions and generate global report

## Usage

### Install
in `requirements.txt`:

### API Config
For openai like api, put `api_config.json` in the root directory with the following content:
```json
{
  "api_key": "your_openai_api_key",
  "base_url": "your_openai_proxy"
}
```

### Run
For demo
```bash
python test_checker.py
python test_reporter.py
```
