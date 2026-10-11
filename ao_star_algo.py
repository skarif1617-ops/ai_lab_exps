class Node:
    def __init__(self, name, node_type, children=None, heuristic=0):
        self.name = name                   # node label
        self.type = node_type              # 'AND' or 'OR'
        self.children = children or []     # child nodes (empty list if leaf)
        self.heuristic = heuristic         # node's own cost
        self.cost = heuristic              # running total cost
        self.solved = False                # has this node been solved?
        self.best_solution = None          # children chosen in the best solution

def ao_star(node):
    if node.solved:                        # already computed, so reuse
        return node.cost
    if not node.children:                  # leaf: cost is just its heuristic
        node.cost = node.heuristic
        node.solved = True
        node.best_solution = []
        return node.cost

    if node.type == 'OR':                  # OR: pick the cheapest child
        min_cost = float('inf')
        best_child = None
        for child in node.children:
            child_cost = ao_star(child)    # solve the child recursively
            if child_cost < min_cost:      # keep the cheapest
                min_cost = child_cost
                best_child = child
        node.cost = node.heuristic + min_cost
        node.best_solution = [best_child] if best_child else []
        node.solved = True
        return node.cost
    else:                                  # AND: every child must be solved
        total_cost = node.heuristic
        for child in node.children:
            total_cost += ao_star(child)   # add all children's costs
        node.cost = total_cost
        node.best_solution = node.children # all children are in the solution
        node.solved = True
        return node.cost

def print_solution(node, indent=0):        # print the chosen solution as a tree
    print("  " * indent + f"{node.name} (Cost: {node.cost}) [{node.type}]")
    for child in (node.best_solution or []):
        print_solution(child, indent + 1)

G = Node('G', 'OR', heuristic=2)           # leaf nodes
H = Node('H', 'OR', heuristic=3)
I = Node('I', 'OR', heuristic=1)
J = Node('J', 'OR', heuristic=5)
D = Node('D', 'AND', children=[G, H], heuristic=1)   # needs G and H
E = Node('E', 'AND', children=[I, J], heuristic=2)   # needs I and J
B = Node('B', 'OR', children=[D, E], heuristic=1)    # D or E
C = Node('C', 'OR', heuristic=10)          # expensive leaf
A = Node('A', 'OR', children=[B, C], heuristic=0)    # root: B or C

total = ao_star(A)                         # compute the optimal cost
print(f"AO* Total Cost: {total}")
print("AO* Solution Graph:")
print_solution(A)