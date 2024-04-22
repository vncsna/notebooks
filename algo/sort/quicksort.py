from random import randint

def quicksort(arr: list[int]):
    if len(arr) <= 1:
        return arr
    left = [a for a in arr if a < arr[-1]]
    right = [a for a in arr if a > arr[-1]]
    middle = [a for a in arr if a == arr[-1]]
    return quicksort(left) + middle + quicksort(right)

quicksort([randint(0, 10) for i in range(10)])
