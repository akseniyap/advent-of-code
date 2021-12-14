data = []

with open('input.txt') as file:
    for line in file:
        data.append(line)

data = list(map(int, data))


def part_one(data):
    diffs = list(map(lambda x, y: x < y, data, data[1:]))
    return len(list(filter(lambda x: x is True, diffs)))

print(part_one(data))


def part_two(data):
    sums = list(map(lambda x, y, z: x + y + z, data, data[1:], data[2:]))
    incrs = list(map(lambda x, y: x < y, sums, sums[1:]))
    return len(list(filter(lambda x: x is True, incrs)))

print(part_two(data))

