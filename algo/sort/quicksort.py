from random import randint

arr = [randint(0, 10) for i in range(10)]


def quicksort1(arr: list[int]):
    if len(arr) <= 1:
        return arr
    left = [a for a in arr if a < arr[-1]]
    right = [a for a in arr if a > arr[-1]]
    middle = [a for a in arr if a == arr[-1]]
    return quicksort1(left) + middle + quicksort1(right)


def quicksort2(arr, left, right):
    if left < right:
        pivot = partition2(arr, left, right)
        quicksort2(arr, left, pivot - 1)
        quicksort2(arr, pivot + 1, right)
    return arr


def partition2(arr, left, right):
    i = left - 1
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


print(quicksort1(arr))
print(quicksort2(arr, 0, len(arr) - 1))
