# Interview Cake
# https://www.interviewcake.com/question/python3/reverse-words


def reverse(msg: list[str]) -> list[str]:
    """Reverse words"""

    def invert(a: int, c: int):
        """Invert characters"""
        b = (a + c) // 2
        for i in range(b - a):
            x, y = a + i, c - i - 1
            msg[x], msg[y] = msg[y], msg[x]
    
    # Reverse characters
    invert(0, len(msg))

    # Get locations
    ends = []
    is_word = False
    for i in range(len(msg)):
        if is_word and msg[i] == " ":
            is_word = False
            ends += [i]
        if not is_word and msg[i] != " ":
            is_word = True
            ends += [i]
    ends += [len(msg)]

    # Reverse words
    for i in range(0, len(ends), 2):
        invert(ends[i], ends[i + 1])

    return msg


# steal pound cake
message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
print(''.join(reverse(message)))
