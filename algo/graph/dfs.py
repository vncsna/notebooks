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


def in_order(node):
    if not node:
        return []
    left = in_order(node.left)
    right = in_order(node.right)
    return left + [node.val] + right


def pre_order(node):
    if not node:
        return []
    left = pre_order(node.left)
    right = pre_order(node.right)
    return [node.val] + left + right


def post_order(node):
    if not node:
        return []
    left = post_order(node.left)
    right = post_order(node.right)
    return left + right + [node.val]


def in_order_i(root):
    if not root:
        return []

    order = []
    stack = []
    current = root
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            node = stack.pop()
            current = node.right
            order.append(node.val)
    return order


def pre_order_i(root):
    if not root:
        return []

    order = []
    stack = [root]
    while stack:
        node = stack.pop(0)
        if node.right:
            stack.insert(0, node.right)
        if node.left:
            stack.insert(0, node.left)        
        order.append(node.val)
    return order


def post_order_i(root):
    if not root:
        return []

    order = []
    stack2 = []
    stack1 = [root]
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        order.append(stack2.pop().val)
    return order


#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   7


print("in", in_order(root))
print("in", in_order_i(root))
print("pre", pre_order(root))
print("pre", pre_order_i(root))
print("post", post_order(root))
print("post", post_order_i(root))
