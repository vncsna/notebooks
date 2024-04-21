# Interview Cake
# https://www.interviewcake.com/question/python3/merge-sorted-arrays

# Review
# Should consider different lenghts

def merge(a: list, b: list) -> list:
    if not a:
        return b
    if not b:
        return a
    i = 0
    j = 0
    c = []
    while i < len(a) or j < len(b):
        if i == len(a):
            c.extend(b[j:])
            break
        if j == len(b):
            c.extend(b[i:])
            break
        if a[i] < b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1
    return c

a_list = [3, 4, 6, 10, 11, 15]
b_list = [1, 5, 8, 12, 14, 19]
print(merge(a_list, b_list))
a_list = [3, 4, 6, 10, 11, 15]
b_list = [1, 5, 8, 12, 14, 19, 23, 42]
print(merge(a_list, b_list))
