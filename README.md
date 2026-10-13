# 22IT702 Lab Experiments

Python implementations and datasets for the **22IT702 Lab Manual**.
All scripts are written directly without function definitions (`def`), providing straightforward procedural executions.

---

## Environment Setup

These experiments run with the Conda environment named `ls`:

```bash
# Activate the environment
conda activate ls

# Or install dependencies from requirements.txt if needed
pip install -r requirements.txt
```

---

## List of Experiments & Files

| Experiment | Title | Script File | Input / Output Files |
| :--- | :--- | :--- | :--- |
| **Exp 1** | Data Pre-processing | [`exp1_data_preprocessing.py`](file:///d:/Projects/aiep/exp1_data_preprocessing.py) | Input: [`sample_data.csv`](file:///d:/Projects/aiep/sample_data.csv)<br>Output: [`cleaned_dataset.csv`](file:///d:/Projects/aiep/cleaned_dataset.csv) |
| **Exp 2** | BFS & DFS Graph Traversal | [`exp2_bfs_dfs.py`](file:///d:/Projects/aiep/exp2_bfs_dfs.py) | In-memory graph (queue BFS & stack DFS) |
| **Exp 3** | Hill Climbing & A* Search (Combined 3A & 3B) | [`exp3_hill_climbing_and_a_star.py`](file:///d:/Projects/aiep/exp3_hill_climbing_and_a_star.py) | Procedural 3A and 3B |
| **Exp 4** | Rule-Based Chatbot | [`exp4_rule_based_chatbot.py`](file:///d:/Projects/aiep/exp4_rule_based_chatbot.py) | Interactive input via terminal |
| **Exp 5** | Inference System | [`exp5_inference_system.py`](file:///d:/Projects/aiep/exp5_inference_system.py) | Forward chaining rules & facts |
| **Exp 6** | N-Queens Problem | [`exp6_n_queens.py`](file:///d:/Projects/aiep/exp6_n_queens.py) | Backtracking on an 8x8 chessboard |

---

## How to Run Each Experiment

### Experiment 1: Data Pre-processing
Reads [`sample_data.csv`](file:///d:/Projects/aiep/sample_data.csv), eliminates `NaN` values and duplicates, then saves the result to [`cleaned_dataset.csv`](file:///d:/Projects/aiep/cleaned_dataset.csv).
```bash
conda run -n ls python exp1_data_preprocessing.py
```

### Experiment 2: Breadth First Search (BFS) & Depth First Search (DFS)
Traverses a directed graph starting from node `'A'` without using `def`.
```bash
conda run -n ls python exp2_bfs_dfs.py
```

### Experiment 3: Hill Climbing & A* Algorithm (Combined 3A & 3B)
Executes both Hill Climbing and the A* search algorithm sequentially in one script without using `def`.
```bash
conda run -n ls python exp3_hill_climbing_and_a_star.py
```

### Experiment 4: Rule-Based Chatbot
An interactive chatbot responding to conversational triggers (`hello`, `how are you`, `what is ai`, `bye`) without using `def`.
```bash
conda run -n ls python exp4_rule_based_chatbot.py
```

### Experiment 5: Inference System
Applies rule-based forward chaining on known facts (`['rainy']`).
```bash
conda run -n ls python exp5_inference_system.py
```

### Experiment 6: N-Queens Problem
Uses iterative backtracking to place 8 non-attacking queens on an $8 \times 8$ board without using `def`.
```bash
conda run -n ls python exp6_n_queens.py
```
