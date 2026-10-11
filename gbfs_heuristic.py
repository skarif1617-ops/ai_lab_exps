from queue import PriorityQueue            # built-in priority queue

graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
         'D': [], 'E': [], 'F': ['G'], 'G': []}
heuristic = {'A': 6, 'B': 4, 'C': 5, 'D': 3, 'E': 2, 'F': 1, 'G': 0}   # h(n) per node

def best_first_search(start, goal):
    visited = set()                        # nodes already expanded
    pq = PriorityQueue()                   # open list
    pq.put((heuristic[start], start))      # insert (h, node)
    path = []                              # order of visited nodes

    print(f"\nStep-by-step traversal:\n{'-'*30}")
    while not pq.empty():                  # until the open list is empty
        h, current = pq.get()              # remove the lowest-h node
        print(f"Visiting Node: {current} (Heuristic: {h})")
        if current in visited:             # duplicates may exist, so skip them
            continue
        visited.add(current)               # mark expanded
        path.append(current)               # record it
        if current == goal:                # goal reached
            print(f"\nGoal Node '{goal}' found!\n")
            return path
        for neighbor in graph[current]:    # add unvisited neighbors
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))
    print("\nGoal not reachable.")
    return path

result_path = best_first_search('A', 'G')  # run from A to G
print("Final Path Traversed:")
print(" -> ".join(result_path))