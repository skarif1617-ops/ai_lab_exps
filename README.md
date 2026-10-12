# Artificial Intelligence Laboratory (23CS31P1)

Python implementations of the experiments from the **III Year, 1st Semester Artificial Intelligence Lab Manual**. Each program implements one AI technique covered in the course: graph search, heuristic search, adversarial search, constraint satisfaction, logical reasoning, and rule-based expert systems.

## Experiments at a glance

| Expt | Experiment | File | Technique |
|------|-----------|------|-----------|
| 1 | Breadth First Search | `bfs.py` | Uninformed search (queue) |
| 2 | Best First Search | `bfs_best.py` | Heuristic search (priority queue) |
| 3 | Depth First Search | `dfs.py` | Uninformed search (recursion/stack) |
| 4 | Heuristic Search | `gbfs_heuristic.py` | Greedy best-first search |
| 5 | A* and AO* algorithms | `a_star_algo.py`, `ao_star_algo.py` | Optimal path / AND-OR graph search |
| 6 | Water-Jug Problem | `water_jug_problem*.py` | State-space search (BFS) |
| 7 | Alpha-Beta Pruning | `alpha_beta_pruning*.py` | Adversarial search (Minimax) |
| 8 | 8-Queens Problem | `8_queens.py` | Backtracking |
| 9 | Meeting Scheduling (Default Reasoning) | `meeting_schedul*.py` | Non-monotonic reasoning |
| 10 | Unification Algorithm | `unification.py` | Predicate logic |
| 11 | Knowledge-Based Expert System | `expert_system.py` | Rule-based inference |
| 12 | 8-Puzzle with heuristics and Tic-Tac-Toe | `8_puzzle_aostar*.py` | Heuristic search and game play |

Files marked with `*` are shortened names; use the full filename in your folder.

## Requirements

- Python 3.8 or newer
- Most programs use only the Python standard library. Check the `import` lines at the top of each file if a module is missing.

## How to run

From the repository folder:

```bash
python bfs.py
```

Replace the filename with any experiment file from the table. Programs run in the terminal and print their results to the console.

---

## Experiment details

### 1. Breadth First Search (`bfs.py`)

**Aim:** Implement BFS on a graph and show the traversal from a specified start node.

**How it works:** Starts at the given node, visits all of its neighbours, then their neighbours, level by level. A queue holds nodes waiting to be visited, and a visited set prevents revisiting.

### 2. Best First Search (`bfs_best.py`)

**Aim:** Find a path in a graph by always expanding the most promising node according to a heuristic.

**How it works:** Keeps a priority queue of frontier nodes ordered by heuristic value and always expands the lowest-value node next.

### 3. Depth First Search (`dfs.py`)

**Aim:** Implement DFS and traverse a graph starting from a specified node.

**How it works:** Follows one branch as deep as possible before backtracking. Each node is marked visited so it isn't processed twice. The program prints each step and the final traversal order.

### 4. Heuristic Search (`gbfs_heuristic.py`)

**Aim:** Find a path from a start node to a goal node using heuristic estimates of the remaining cost to the goal.

**How it works:** Greedy Best-First Search expands the node whose heuristic value h(n) is smallest, which is the one that appears closest to the goal.

### 5. A* and AO* Algorithms (`a_star_algo.py`, `ao_star_algo.py`)

**Aim:**
- **A\*:** Find the shortest path from a start node to a goal node.
- **AO\*:** Find the optimal solution graph in an AND-OR graph, considering heuristic and solve-cost values.

**How it works:**
- **A\*** ranks nodes by f(n) = g(n) + h(n), where g is the cost so far and h is the heuristic estimate.
- **AO\*** handles AND-OR graphs, where a goal may need several sub-goals to be solved together (AND) or only one of several alternatives (OR).

### 6. Water-Jug Problem (`water_jug_problem*.py`)

**Aim:** Find a sequence of fill, empty, and pour operations that measures an exact target amount using two jugs of given capacities.

**How it works:** Each state is the water level in both jugs. A BFS explores all reachable states until the target amount appears in one of the jugs, then prints the path that reaches it.

### 7. Alpha-Beta Pruning (`alpha_beta_pruning*.py`)

**Aim:** Implement Alpha-Beta Pruning to optimise the Minimax strategy for two-player games.

**How it works:** Minimax searches the game tree for the best move for each player. Alpha-Beta keeps track of the best values found so far for each side and skips branches that cannot change the final decision, so fewer nodes are evaluated.

### 8. 8-Queens Problem (`8_queens.py`)

**Aim:** Place eight queens on an 8×8 chessboard so that no two queens attack each other.

**How it works:** Backtracking places one queen per row. If a placement causes a conflict in its row, column, or diagonal, the program undoes it and tries the next column.

### 9. Meeting Scheduling with Default Reasoning (`meeting_schedul*.py`)

**Aim:** Schedule a meeting among five busy people and output the day, time, and place.

**How it works:** Uses default reasoning, where each person is assumed to be available unless their schedule says otherwise. Conflicting assumptions are resolved, and the program outputs one meeting slot that works for everyone.

### 10. Unification Algorithm (`unification.py`)

**Aim:** Implement unification, which finds a substitution (a unifier) that makes two logical expressions identical.

**How it works:** Compares the two expressions term by term. Variables are bound to matching terms, and the algorithm returns the substitution if one exists or reports failure if the expressions cannot be made identical.

### 11. Knowledge-Based Expert System (`expert_system.py`)

**Aim:** Build a knowledge base of facts and rules about a specialised domain and use an inference engine to reach conclusions.

**How it works:** Stores known facts and if-then rules. The inference engine applies the rules to the facts, and the user's answers to yes/no questions can lead to a conclusion. The manual describes both a symptom-based diagnosis system and an animal classification system.

### 12. 8-Puzzle with Heuristics and Tic-Tac-Toe (`8_puzzle_aostar*.py`)

**Aim:** Solve the 8-puzzle using different heuristics (Manhattan distance and misplaced tiles), then let the user play Tic-Tac-Toe. At the end, the program reports the number of nodes generated and cutoff values at each stage as a table.

**How it works:** A* search with each heuristic solves the puzzle. The program records nodes generated and cutoff values for each run and prints them in a table so the heuristics can be compared.

---

## Course information

**Course objectives:** Study the concepts of AI, learn problem-solving methods using AI, and understand expert systems and machine learning.

**Course outcomes:**
1. Understand the basics of AI and different types of agent characteristics.
2. Know various problem-solving agents and their behaviour in real-world environments.
3. Understand and apply the fundamentals of AI search algorithms.
4. Gain knowledge in adversarial search methods.
5. Draw inferences based on logical reasoning.
6. Apply different learning techniques for future implementation.

**Textbooks:**
- Prateek Joshi, *Artificial Intelligence with Python*, Packt Publishing, 2017.
- Perry Xiao, *Artificial Intelligence Programming with Python: From Zero to Hero*, Wiley, 2022.

**References:**
- Stuart J. Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed., Pearson, 2020.
- Martin C. Brown, *Python: The Complete Reference*, 4th ed., McGraw-Hill, 2018.
- R. Nageswara Rao, *Core Python Programming*, Dreamtech Press, 2018.