with open("data.txt") as f:
    _input = f.read().splitlines()

def find_max(pack):
    numbers = [0] * 12
    for n in pack:                                          # for every number in pack
        for idx, val in enumerate(numbers):                 # for every index and value in numbers
            next_idx = idx + 1                              # define next index
            if next_idx < len(numbers) and val < numbers[next_idx]:         # check if value is smaller than next
                numbers[idx] = numbers[next_idx]
                numbers[next_idx] = 0
        if int(n) > numbers[-1]:                             # check if number is smaller than last number
            numbers[-1] = int(n)
    print(numbers)
    return int("".join(map(str, numbers)))                        # return numbers as one number [4, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8] should return 434234234278


print(sum(find_max(pack) for pack in _input))