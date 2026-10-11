import heapq                               # priority queue for A*
from copy import deepcopy                  # to copy the board when making a move

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]    # 0 = blank
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]        # blank moves: right, down, left, up

class PuzzleNode:                          # one search node
    def __init__(self, state, parent=None, depth=0, cost=0):
        self.state = state                 # 3x3 board
        self.parent = parent               # node we came from
        self.depth = depth                 # g(n): moves made so far
        self.cost = cost                   # f(n) = g(n) + h(n)
    def __lt__(self, other):               # lets heapq order nodes by f
        return self.cost < other.cost

def find_blank(state):                     # locate the empty tile
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def manhattan_distance(state):             # heuristic 1
    dist = 0
    for i in range(3):
        for j in range(3):
            v = state[i][j]
            if v != 0:                     # ignore the blank
                dist += abs((v - 1) // 3 - i) + abs((v - 1) % 3 - j)   # rows + cols from home
    return dist

def misplaced_tiles(state):                # heuristic 2
    return sum(1 for i in range(3) for j in range(3)
               if state[i][j] != 0 and state[i][j] != goal_state[i][j])

def generate_children(node):               # all boards reachable in one move
    children = []
    x, y = find_blank(node.state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy            # new blank position
        if 0 <= nx < 3 and 0 <= ny < 3:    # must stay on the board
            s = deepcopy(node.state)       # copy so the parent is unchanged
            s[x][y], s[nx][ny] = s[nx][ny], s[x][y]    # slide the tile
            children.append(PuzzleNode(s, node, node.depth + 1))
    return children

def a_star(start, h):
    root = PuzzleNode(start)
    root.cost = h(start)                   # f(root) = 0 + h
    frontier = [root]                      # open list
    explored = set()                       # closed list
    generated = 1                          # count the root
    table = []                             # (depth, f-cost) for each expansion

    while frontier:
        cur = heapq.heappop(frontier)      # lowest f first
        if cur.state == goal_state:        # solved
            return cur, generated, table
        explored.add(tuple(map(tuple, cur.state)))   # lists cannot go in a set, so use tuples
        table.append((cur.depth, cur.cost))          # record the cutoff value
        for child in generate_children(cur):
            if tuple(map(tuple, child.state)) not in explored:
                child.cost = child.depth + h(child.state)   # f = g + h
                heapq.heappush(frontier, child)
                generated += 1             # one more node generated
    return None, generated, table          # unsolvable

def print_path(node):                      # show the solution moves
    path = []
    while node:                            # walk back to the start
        path.append(node.state)
        node = node.parent
    for s in reversed(path):               # print start to goal
        for row in s:
            print(row)
        print()

def show_table(table):                     # print the cutoff table
    print("Depth | f-cost (cutoff)")
    print("------+----------------")
    for d, c in table:
        print(f"{d:^5} | {c:^8}")

# ---------------- Tic-Tac-Toe ----------------
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, mark):
    for row in board:                      # any full row
        if all(c == mark for c in row):
            return True
    for col in range(3):                   # any full column
        if all(board[r][col] == mark for r in range(3)):
            return True
    return (all(board[i][i] == mark for i in range(3)) or        # main diagonal
            all(board[i][2 - i] == mark for i in range(3)))      # other diagonal

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]  # empty 3x3 grid
    count = 0                              # moves played
    player = "X"                           # X starts
    while count < 9:                       # at most 9 moves
        print_board(board)
        print(f"Player {player}'s turn")
        x = int(input("Enter row (0-2): "))
        y = int(input("Enter col (0-2): "))
        if board[x][y] == " ":             # cell is free
            board[x][y] = player
            count += 1
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                return
            player = "O" if player == "X" else "X"   # switch player
        else:
            print("Cell already taken!")
    print_board(board)
    print("Game is a draw!")

if __name__ == "__main__":
    start = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]        # solvable start (2 moves)
    for name, h in [("Manhattan Distance", manhattan_distance),
                    ("Misplaced Tiles", misplaced_tiles)]:
        print(f"\nSolving using {name}...")
        node, gen, table = a_star(start, h)
        print_path(node)
        print("Nodes generated:", gen)
        show_table(table)
    print("\nNow, Play Tic-Tac-Toe!")
    tic_tac_toe()