# Interview Cake
# https://www.interviewcake.com/question/python3/linked-list-cycles

# Review
# Remember the floyd approach

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next  = None


head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)
head.next.next.next.next.next = head.next.next


def has_cycle_by_hash(head: LinkedListNode):
    """
    Time O(n)
    Space O(n)
    """
    marked = set()
    while head:
        if head in marked:
            return True
        marked.add(head)
        head = head.next
    return False


def has_cycle_by_floyd(head: LinkedListNode):
    """
    Time O(n)
    Space O(1)
    """
    node_fast = head
    node_slow = head

    while node_slow and node_fast:
        node_slow = node_slow.next
        node_fast = node_fast.next.next if node_fast.next else None

        if node_slow and node_fast and node_slow == node_fast:
            return True

    return False


assert has_cycle_by_hash(head)
assert has_cycle_by_floyd(head)
