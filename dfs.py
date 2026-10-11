
def dfs(graph, start, visited=None, traversal=None, step=1):
    if visited is None:
        visited = set()
        traversal = []
        print(f"Start DFS from node: {start}\n")

    visited.add(start)
    traversal.append(start)

    print(f"Step {step}: Visit node {start}")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal, step + 1)

    if step == 1:
        print("\nFinal DFS Traversal:", " -> ".join(traversal))


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

dfs(graph, 'A')