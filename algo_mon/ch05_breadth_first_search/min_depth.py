from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_min_depth(root: Node) -> int:
    queue = deque([root]) # at least one element in the queue to kick start bfs
    depth = -1 # we start from -1 because popping root will add 1 depth
    while len(queue) > 0: # as long as there is element in the queue
        depth += 1
        n = len(queue) # number of nodes in current level
        for _ in range(n): # dequeue each node in the current level
            node = queue.popleft()
            if node.left is None and node.right is None: # found leaf node, early return
                return depth
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
    return depth

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = binary_tree_min_depth(root)
    print(res)