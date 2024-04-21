# Interview Cake
# https://www.interviewcake.com/question/python3/shuffle

# Review
# shuffle_inplace is not a uniform distribution

from random import randint

def shuffle_inplace(arr):
    rnd = lambda: randint(0, len(arr)- 1)
    rnd = [rnd() for _ in range(len(arr))]
    for i, j in enumerate(rnd):
        aux = arr[i]
        arr[i] = arr[j]
        arr[j] = aux
    return arr


print(shuffle_inplace(list(range(0, 4))))
print(shuffle_inplace(list(range(0, 8))))
print(shuffle_inplace(list(range(0, 16))))
