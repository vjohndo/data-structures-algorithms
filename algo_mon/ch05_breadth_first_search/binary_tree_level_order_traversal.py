from collections import deque
from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    res = []
    queue = deque([root]) # at least one element in the queue to kick start bfs
    while len(queue) > 0: # as long as there is element in the queue
        n = len(queue) # number of nodes in current level, see explanation above
        new_level = []
        for _ in range(n): # dequeue each node in the current level
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]: # enqueue non-null children
                if child is not None:
                    queue.append(child)
        res.append(new_level)
    return res

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = level_order_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))