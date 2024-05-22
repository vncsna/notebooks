from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def topView(root: Optional[TreeNode]) -> List[int]:
    view = {}

    def dfs(node: TreeNode, pos: int):
        if not node:
            return
        if pos not in view:
            view[pos] = node.val
        dfs(node.left, pos - 1)
        dfs(node.right, pos + 1)

    dfs(root, 0)

    view = [(k, v) for k, v in view.items()]
    view = sorted(view, key=lambda k: k[0])
    view = [v[1] for v in view]

    return view


def bottomView(root: Optional[TreeNode]) -> List[int]:
    view = {}
    queue = [(root, 0)]

    while queue:
        node, pos = queue.pop(0)

        if node.left:
            queue.append((node.left, pos - 1))

        if node.right:
            queue.append((node.right, pos + 1))

        view[pos] = node.val

    view = [(k, v) for k, v in view.items()]
    view = sorted(view, key=lambda k: k[0])
    view = [v[1] for v in view]

    return view


def leftSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    value = []
    queue  = [(root, 0)]

    while queue:
        node, level = queue.pop(0)

        if len(value) < level + 1:
            value.append(0)

        if node.right:
            queue.append((node.right, level + 1))

        if node.left:
            queue.append((node.left, level + 1))
        
        value[level] = node.val
        
    return value


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    value = []
    queue  = [(root, 0)]

    while queue:
        node, level = queue.pop(0)

        if len(value) < level + 1:
            value.append(0)
        
        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))
        
        value[level] = node.val
        
    return value



#    1
#  2   3
#   5   4
node_5 = TreeNode(val=5)
node_4 = TreeNode(val=4)
node_3 = TreeNode(val=3, right=node_4)
node_2 = TreeNode(val=2, right=node_5)
node_1 = TreeNode(val=1, left=node_2, right=node_3)

assert topView(node_1) == [2, 1, 3, 4]
assert bottomView(node_1) == [2, 5, 3, 4]
assert leftSideView(node_1) == [1, 2, 5]
assert rightSideView(node_1) == [1, 3, 4]
