import math

def alpha_beta(depth, node_index, is_max, values, alpha, beta):
    if depth == 3:                         # leaf level of a depth-3 tree
        return values[node_index]          # return the leaf's value

    if is_max:                             # MAX player's turn
        best = -math.inf                   # start with worst possible
        for i in range(2):                 # two children per node
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)          # keep the largest value
            alpha = max(alpha, val)        # update MAX's guaranteed value
            if beta <= alpha:              # MIN above would never allow this branch
                break                      # prune the remaining children
        return best
    else:                                  # MIN player's turn
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)          # keep the smallest value
            beta = min(beta, val)          # update MIN's guaranteed value
            if beta <= alpha:              # MAX above would never allow this branch
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]         # 8 leaf values
result = alpha_beta(0, 0, True, values, -math.inf, math.inf)   # root is MAX
print("The optimal value is:", result)