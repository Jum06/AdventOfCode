with open("data.txt") as f:
    _input = f.read().splitlines()

def find_max(pack):
    num1, num2 = 0, 0
    for n in pack:
        if num1 < num2:
            num1 = num2
            num2 = 0
        if int(n) > num2:
            num2 = int(n)
    print(res := int(str(num1) + str(num2)))
    return res


print(sum(find_max(pack) for pack in _input))




# def find_max(pack: str) -> int:
#     digits = [int(c) for c in pack]
#     # Track the largest possible tens digit seen so far, then pair it with each
#     # later digit (ones place) to keep the best chronological two‑digit number.
#     tens_max = digits[0]
#     best = -1
#
#     for ones in digits[1:]:
#         best = max(best, tens_max * 10 + ones)
#         if ones > tens_max:
#             tens_max = ones
#
#     return best
#
#
# print(sum(find_max(pack) for pack in _input))
