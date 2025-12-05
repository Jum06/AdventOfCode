with open("data.txt") as f:
    sec1, sec2 = f.read().strip().split("\n\n")
    ranges = [list(map(int, line.split("-"))) for line in sec1.splitlines()]
    ids = [int(line) for line in sec2.splitlines()]

# def check_id(i):
#     for r in ranges:
#         if r[0] <= i <= r[1]:
#             return True
#     return False
#
# print(sum(check_id(i) for i in ids))
#

print(sum(any(a <= i <= b for a, b in ranges) for i in ids))

