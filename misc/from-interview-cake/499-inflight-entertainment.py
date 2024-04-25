# Interview Cake
# https://www.interviewcake.com/question/python3/inflight-entertainment

# Review
# O(n) Save the opposite in dict
# O(n²) Brute force with two loops


def has_sum(arr: list[int], target: int):
    diff = {}
    for a in arr:
        if a in diff:
            return True
        diff[target - a] = True
    return False

assert has_sum([1,2,3,4,5,6], 7)
