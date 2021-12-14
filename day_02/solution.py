data = []                                                                       
                                                                                
with open('input.txt') as file:                                                 
    for line in file:                                                           
        data.append(line)                                                       

data = list(map(lambda x: x.strip().split(), data))
 

def part_one(data):
    horizontal, depth = 0, 0

    for direction, value in data:
        value = int(value)

        if direction == 'forward':
            horizontal += value
        elif direction == 'down':
            depth += value
        else:
            depth -= value

    return horizontal * depth


print(part_one(data))


def part_two(data):
    horizontal, depth, aim = 0, 0, 0

    for direction, value in data:
        value = int(value)

        if direction == 'forward':
            horizontal += value
            depth += aim * value
        elif direction == 'down':
            aim += value
        else:
            aim -= value

    return horizontal * depth

print(part_two(data))

