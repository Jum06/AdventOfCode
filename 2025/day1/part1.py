with open("data.txt") as f:
    _input = f.read().splitlines()

zeros = 0
current = 50

for line in _input:
    number = int(line[1:])
    # print(number)
    if line[0] == "R":
        current = (current + number) % 100
    else:
        current = (current - number) % 100

    if current == 0:
        zeros += 1
    print(current)

print(zeros)


c = 50
print(sum((c := (c + (1, -1)[l[0] == "L"] * int(l[1:])) % 100) == 0 for l in open("data.txt")))