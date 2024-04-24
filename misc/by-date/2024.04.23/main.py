# Review
# Avoid enumerator in subarray
# Include previous case in minimum


def find(nums, target):
    """Calculate sum of three numbers nearest target"""

    if not nums or not target:
        return 0

    arr = nums[:3]
    dif = abs(sum(arr) - target)
    for i in range(3, len(nums)):
        s0 = [nums[i], arr[1], arr[2]]
        s1 = [arr[0], nums[i], arr[2]]
        s2 = [arr[0], arr[1], nums[i]]

        dif0 = abs(sum(s0) - target)
        dif1 = abs(sum(s1) - target)
        dif2 = abs(sum(s2) - target)
        
        dif = min(dif, dif0, dif1, dif2)

        if dif0 == dif:
            arr[0] = nums[i]
        elif dif1 == dif:
            arr[1] = nums[i]
        elif dif2 == dif:
            arr[2] = nums[i]

    return sum(arr)


assert find([0, 1, 2], 4) in [3]
assert find([-1, 2, 1, -4], 1) in [2]
assert find([0, 1, 2, 4, 6], 4) in [3, 5]
