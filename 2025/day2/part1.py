import re

with open("data.txt") as f:
    s = f.read().strip()
    ranges = []
    if s:
        ranges = [list(map(int, part.split("-"))) for part in s.split(",")]

sumOfMissInputs = 0
pattern1 = r"^([0-9]+)\1$"            # part1
pattern2 = r"^([0-9]+)\1+$"           # part2

for r in ranges:
    for i in range(r[0], r[1]+1):
        if re.match(pattern1, str(i)):
            sumOfMissInputs += i

print(sumOfMissInputs)