import heapq                               # heapq = priority queue (smallest value first)

def best_first_search(graph, start, goal, heuristic):
    visited = set()                        # nodes already queued or expanded
    priority_queue = []                    # the open list
    heapq.heappush(priority_queue, (heuristic[start], start))  # push (h-value, node)
    parent = {start: None}                 # remembers how we reached each node

    while priority_queue:                  # while there are nodes to explore
        _, current = heapq.heappop(priority_queue)   # pop node with LOWEST h

        if current == goal:                # goal test
            path = []                      # will hold the route
            while current:                 # walk back using parent links
                path.append(current)
                current = parent[current]  # start's parent is None, which ends the loop
            path.reverse()                 # was goal->start, so flip it
            return path

        visited.add(current)               # mark as expanded
        for neighbor in graph[current]:    # check neighbors
            if neighbor not in visited:
                parent[neighbor] = current # remember where we came from
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                visited.add(neighbor)      # avoid pushing it twice
    return None                            # queue empty means no path

graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
         'D': [], 'E': ['F'], 'F': []}     # directed graph
heuristic = {'A': 5, 'B': 4, 'C': 2, 'D': 6, 'E': 1, 'F': 0}  # estimated distance to F

path = best_first_search(graph, 'A', 'F', heuristic)
if path:
    print("Path found by Best First Search:", ' -> '.join(path))
else:
    print("No path found")