data = []                                                                       
                                                                                
with open('input.txt') as file:                                                 
    for line in file:                                                           
        data.append(line) 

data = data[0].strip().split(',')
data = list(map(int, data))


def part_one(data):
    min_fuel = sum(data)

    for i in range(0, max(data) + 1):
        fuel = list(map(lambda x: abs(x - i), data))
        tmp = sum(fuel)
        min_fuel = min(min_fuel, tmp)

    return min_fuel

print(part_one(data))


def part_two(data):
    min_fuel = sum(list(map(lambda x: sum(range(0, x + 1)), data)))

    for i in range(0, max(data) + 1):
        fuel = list(map(lambda x: sum(range(0, abs(x - i) + 1)), data))
        tmp = sum(fuel)
        min_fuel = min(min_fuel, tmp)

    return min_fuel

print(part_two(data))

