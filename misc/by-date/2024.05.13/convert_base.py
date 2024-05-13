def to_decimal_from_base_n(num: str, base: int) -> int:
    decimal = 0
    for n in num:
        decimal = decimal * base + int(n)
    return decimal


def to_base_n_from_decimal(num: int, base: int) -> int:
    if num < base:
        return num
    ans = []
    while num > 0:
        ans.append(str(num % base))
        num = num // base
    return int("".join(ans[::-1]))


assert to_decimal_from_base_n("0", 2)  == 0
assert to_decimal_from_base_n("1", 2)  == 1
assert to_decimal_from_base_n("10", 2) == 2
assert to_decimal_from_base_n("11", 2) == 3

assert to_base_n_from_decimal(0, 6) == 0
assert to_base_n_from_decimal(6, 6) == 10
