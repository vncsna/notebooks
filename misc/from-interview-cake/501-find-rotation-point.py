# Interview Cake
# https://www.interviewcake.com/question/python/find-rotation-point


def find_v1(words):
    for i in range(len(words) - 1):
        if words[i] > words[i + 1]:
            break
    return i + 1


def find_v2(words):
    a, c = 0, len(words) - 1

    while a < c:
        b = a + ((c - a) // 2)
        if words[0] <= words[b]:
            a = b
        else:
            c = b
        
        if a + 1 == c:
            return c

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here in position 5
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

assert find_v1(words) == 5, find_v1(words)
assert find_v2(words) == 5, find_v2(words)
