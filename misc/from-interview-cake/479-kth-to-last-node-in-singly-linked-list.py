# Interview Cake
# https://www.interviewcake.com/question/python3/kth-to-last-node-in-singly-linked-list

# Review
# The answer did not store values
# just went back to iteration after getting its length

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# By loop
def get_kth_to_last_node(a, n):
    k = 0
    node = a
    values = []
    while node.next:
        values.append(node.value)
        node = node.next
        k += 1
    return values[k - n + 1]
print(get_kth_to_last_node(a, 2))

# By recursion
def get_kth_to_last_node(a, n):
    if not a.next:
        return a, 1
    node, pos = get_kth_to_last_node(a.next, n)
    if pos == n:
        return node, pos
    else:
        return a, pos + 1

node, _ = get_kth_to_last_node(a, 2)
print(node.value)
