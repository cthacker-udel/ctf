from unittest import TestCase

ALPHA = float('-inf')
BETA = float('inf')

def get_alpha(node):
    if node is not None:
        return node[0]
    
    return float('-inf')
    
def get_beta(node):
    if node is not None:
        return node[1]
    
    return float('inf')

BASE_PAIR = (ALPHA, BETA)

MAX_NODE = [BASE_PAIR, [0, 0]]
MIN_NODE = [BASE_PAIR, MAX_NODE]
ROOT_NODE = [BASE_PAIR, MIN_NODE, MIN_NODE, MIN_NODE]

tests = [["2 4 13 11 1 3 3 7 3 3 2 2", "3 6 7 10 11"], ["1 4 2 6 8 7 3 7 2 3 2 2", "10 11"], ["15 4 12 16 10 7 3 1 2 3 2 2", "6 7 10 11"], ["1 4 12 16 1 7 3 1 2 8 2 2", "3"], ["1 4 12 16 1 7 3 1 2 8 10 2", "3 11"]]

def alpha_beta_pruning(values, terminal_depth = 0):
    # Represents the tree
    depth_children = {
        0: 3,
        1: 2,
        2: 2
    }

    tree = ROOT_NODE
    curr_ind = 0
    visited_nodes = set()

    def max_value(curr_node, alpha, beta, parent = None):
        if type(curr_node) is int:  # Terminal nodes
            return curr_node

        best_value = get_alpha(parent)
        for child in curr_node:
            if type(child) is list:
                child_value = min_value(child, alpha, beta, curr_node[0])
                if child_value >= beta:
                    return best_value
                alpha = max(alpha, best_value)
                curr_node[0][0] = alpha
        return best_value

    def min_value(curr_node, alpha, beta, parent = None):
        if type(curr_node) is int:  # Terminal nodes
            return curr_node

        best_value = get_alpha(parent)
        for child in curr_node:
            if type(child) is list:
                child_value = max_value(child, alpha, beta, curr_node[0])
                if child_value <= alpha:
                    return best_value
                alpha = min(beta, best_value)
                curr_node[0][1] = beta
        return best_value

    best_value = max_value(tree, ALPHA, BETA, tree[0])
    return None


def main(inp = False):

    test_case = TestCase()

    input_values = ''
    if inp:
        input_values = input("Enter 12 numbers separated by space: ")
        values = list(map(int, input_values.split()))
        nodes = alpha_beta_pruning(values)
    else:
        for each_test in tests:
            input_values = each_test[0]
            values = list(map(int, input_values.split()))
            nodes = alpha_beta_pruning(values, 3)
            stringified_nodes =[str(x) for x in sorted(nodes)]
            test_case.assertEqual(' '.join(stringified_nodes), each_test[1])


if __name__ == "__main__":
    main(False)