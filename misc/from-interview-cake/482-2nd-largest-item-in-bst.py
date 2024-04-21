# Interview Cake
# https://www.interviewcake.com/question/python3/second-largest-item-in-bst


class BinaryTreeNode(object):
    def __init__(self, value):
        self.left  = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            if not self.left:
                self.left = BinaryTreeNode(value)
                return self.left
        if value > self.value:
            if self.right:
                return self.right.insert(value)
            if not self.right:
                self.right = BinaryTreeNode(value)
                return self.right
        return self.value

    def largest(self):
        if self.right:
            return self.right.largest()
        if not self.right:
            return self.value

    def largest_2nd(self, parent: int = None):
        if self.right:
            return self.right.largest_2nd(self.value)
        if not self.right and self.left:
            return self.left.largest()
        if not self.right and not self.left:
            return parent or self.value


bst = BinaryTreeNode(11)
bst.insert(20)
bst.insert(17)
bst.insert(13)
bst.insert(5)
bst.insert(3)
bst.insert(2)

print(bst.largest())
print(bst.largest_2nd())
