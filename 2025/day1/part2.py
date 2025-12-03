with open("data.txt") as f:
    _input = f.read().splitlines()

zeros = 0
current = 50

for line in _input:
    numberToAdd = int(line[1:])
    if line[0] == "R":
        current = (current + numberToAdd)
        zeros = zeros + (current // 100)
    else:
        if current == 0:
            zeros -= 1
        current = (current - numberToAdd)
        zeros = zeros - (current // 100)
        if current <= 0 and (-current) % 100 == 0:
            zeros += 1
    current = current % 100

    print(current)

print(zeros)

# Codex optimized
c = 50
print(
    sum(
        -(s and c == 0)
        + (1 - 2 * s) * ((c := c + (1, -1)[s] * int(l[1:])) // 100)
        + (s and c <= 0 and c % 100 == 0)
        + (c := c % 100) * 0
        for l in open("data.txt")
        for s in [l[0] == "L"]
    )
)