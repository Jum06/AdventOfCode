with open("data.txt") as f:
    sec1, sec2 = f.read().strip().split("\n\n")
    ranges = [list(map(int, line.split("-"))) for line in sec1.splitlines()]


print()
