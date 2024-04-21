# Interview Cake
# https://www.interviewcake.com/question/python3/bracket-validator

# Review
# It worked well after stack tip


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def validate(chars: str):
    open_ = "([{"
    close = ")]}"
    stack = Stack()
    for c in chars:
        if c in open_:
            stack.push(c)
        if c in close:
            if stack.pop() != open_[close.index(c)]:
                return False
    return True


print(validate("{}"), True)
print(validate("{[}"), False)
print(validate("{[]()}"), True)
print(validate("{[()])}"), False)
