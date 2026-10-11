from collections import deque

def water_jug_bfs(cap1, cap2, target):
    start = (0, 0)                         # both jugs empty
    queue = deque([start])                 # BFS queue of states
    visited = set([start])                 # states already seen
    parent = {start: None}                 # for path reconstruction

    while queue:
        jug1, jug2 = queue.popleft()       # current state

        if jug1 == target or jug2 == target:   # goal test
            path = []
            state = (jug1, jug2)
            while state:                   # follow parents back to start
                path.append(state)
                state = parent[state]
            path.reverse()
            return path

        states = set()                     # all states reachable in one move
        states.add((cap1, jug2))           # fill jug 1
        states.add((jug1, cap2))           # fill jug 2
        states.add((0, jug2))              # empty jug 1
        states.add((jug1, 0))              # empty jug 2
        pour12 = min(jug1, cap2 - jug2)    # amount that fits when pouring 1 into 2
        states.add((jug1 - pour12, jug2 + pour12))
        pour21 = min(jug2, cap1 - jug1)    # amount that fits when pouring 2 into 1
        states.add((jug1 + pour21, jug2 - pour21))

        for state in states:               # queue the new states
            if state not in visited:
                visited.add(state)
                parent[state] = (jug1, jug2)
                queue.append(state)
    return None                            # no way to measure the target

if __name__ == "__main__":
    solution = water_jug_bfs(4, 3, 2)      # jugs of 4 L and 3 L, target 2 L
    if solution:
        print("Solution to get 2 liters:")
        for step, (j1, j2) in enumerate(solution):
            print(f"Step {step}: Jug1 = {j1}L, Jug2 = {j2}L")
    else:
        print("No solution found.")