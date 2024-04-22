from random import randint

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    arr = []
    while left and right:
        if left[0] < right[0]:
            arr.append(left.pop(0))
        else:
            arr.append(right.pop(0))
    arr.extend(left)
    arr.extend(right)
    return arr


mergesort([randint(0, 10) for i in range(10)])
