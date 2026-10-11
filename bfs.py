
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    traversal = []

    print(f"Start BFS from node: {start}\n")
    step = 1

    while queue:
        vertex = queue.popleft()
        traversal.append(vertex)

        print(f"Step {step}: Visit node {vertex}")
        step += 1

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"    Add node {neighbor} to queue")

        print(f"    Current queue: {list(queue)}\n")
        
        print("Final BFS Traversal:", '->'.join(traversal))

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')