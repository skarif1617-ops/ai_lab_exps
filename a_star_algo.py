from heapq import heappush, heappop        # priority queue functions

def a_star(graph, heuristics, start, goal):
    open_list = []                         # open list ordered by f = g + h
    heappush(open_list, (heuristics[start], start))   # f(start) = 0 + h(start)

    g_score = {node: float('inf') for node in graph}  # best known cost to each node
    g_score[start] = 0                     # cost to reach start is 0
    came_from = {}                         # parent links for path rebuilding

    while open_list:
        current_f, current = heappop(open_list)       # node with smallest f

        if current == goal:                # goal reached
            path = []
            while current in came_from:    # walk back to start
                path.append(current)
                current = came_from[current]
            path.append(start)             # add the start node
            path.reverse()                 # put in forward order
            return path, g_score[goal]     # return path and total cost

        for neighbor, cost in graph[current].items():  # neighbors with edge costs
            tentative_g = g_score[current] + cost      # cost via current node
            if tentative_g < g_score[neighbor]:        # found a cheaper way?
                came_from[neighbor] = current          # update parent
                g_score[neighbor] = tentative_g        # update best cost
                f_score = tentative_g + heuristics[neighbor]   # f = g + h
                heappush(open_list, (f_score, neighbor))
    return None, float('inf')              # no path exists

graph = {                                  # {node: {neighbor: edge cost}}
    'S': {'A': 1, 'B': 4},
    'A': {'C': 2, 'D': 5},
    'B': {'D': 1},
    'C': {'G': 5},
    'D': {'G': 2},
    'G': {}
}
heuristics = {'S': 7, 'A': 6, 'B': 2, 'C': 1, 'D': 0, 'G': 0}   # estimates to G

path, cost = a_star(graph, heuristics, 'S', 'G')
print("Shortest path:", path)
print("Total cost:", cost)