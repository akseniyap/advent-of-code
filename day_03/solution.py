data = []

with open('input.txt') as file:
    for line in file:
        data.append(line)

data = list(map(lambda x: list(x.strip()), data))


def part_one(data):
    firsts = [el[0] for el in data]
    seconds = [el[1] for el in data]
    by_positions = [[el[i] for el in data] for i in range(0, 12)]
    
    gamma = []
    epsilon = []
    for element in by_positions:
        zeroes = element.count('0')
        ones = element.count('1')
        bigger = '1' if ones > zeroes else '0'
        smaller = '1' if ones < zeroes else '0'

        gamma.append(bigger)
        epsilon.append(smaller)

    gamma_rate = int(''.join(gamma), 2)
    epsilon_rate = int(''.join(epsilon), 2)

    return gamma_rate * epsilon_rate

    
print(part_one(data))


def part_two(data):
    i = 0
    oxygen = [*data]
    while len(oxygen) != 1:
        zeroes = [el for el in oxygen if el[i] == '0']
        ones   = [el for el in oxygen if el[i] == '1']

        if len(ones) >= len(zeroes):
            oxygen = ones
        else:
            oxygen = zeroes
        i += 1

    i = 0
    co2 = [*data]
    while len(co2) != 1:
        zeroes = [el for el in co2 if el[i] == '0']
        ones   = [el for el in co2 if el[i] == '1']

        if len(zeroes) <= len(ones):
            co2 = zeroes
        else:
            co2 = ones
        i += 1

    oxygen_generator_rating = int(''.join(oxygen[0]), 2)
    co2_scrubber_rating = int(''.join(co2[0]), 2)

    return oxygen_generator_rating * co2_scrubber_rating


print(part_two(data))

