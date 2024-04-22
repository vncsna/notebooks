from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: "TreeNode" = None
    right: "TreeNode" = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


def bfs(queue, result):
    if not queue:
        return result

    node = queue.pop(0)
    result.append(node.val)

    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
    
    return bfs(queue, result)


#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   7


print("bfs", bfs([root], []))
