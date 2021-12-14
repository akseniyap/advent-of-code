data = []

with open('day_08/input.txt') as file:
    for line in file:
        data.append(line)

data = list(map(lambda x: x.strip().split(" "), data))
#print(data)

def part_one(data):
    count_simple_numbers = 0

    for line in data:
        output = line[-4:]
        foo = list(map(lambda x: len(x), output))
        count_simple_numbers += (foo.count(2) + foo.count(3) + foo.count(4) + foo.count(7))

    return count_simple_numbers

print(part_one(data))


def part_two(data):
    four_digits = []
    for line in data:
        line = list(map(lambda el: "".join(sorted(el)), line))
        input, output = line[0:10], line[11:]

        one = [el for el in input if len(el) == 2][0]
        four = [el for el in input if len(el) == 4][0]
        seven = [el for el in input if len(el) == 3][0]
        eight = [el for el in input if len(el) == 7][0]

        top_line = list(set(seven) - set(one))[0]
        part_nine = "".join(sorted(four + top_line))
        nine = [el for el in input if len(el) == 6 and len(set(el)-set(part_nine)) == 1][0]

        bottom_line = list(set(nine) - set(four) - set(top_line))[0]
        three = [el for el in input if len(el) == 5 and len(set(el)-{top_line, bottom_line}-set(one)) == 1][0]

        middle_line = list(set(three) - set(one) - {top_line, bottom_line})[0]
        zero = "".join(sorted(set(eight) - {middle_line}))

        six = [el for el in input if len(el) == 6 and el != zero and el != nine][0]

        top_rigth_line = list(set(eight) - set(six))[0]
        two = [el for el in input if len(el) == 5 and el != three and top_rigth_line in el][0]
        five = [el for el in input if len(el) == 5 and el != three and el != two][0]

        foo = {one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, zero: 0}

        four_digits.append(foo[output[0]]*1000 + foo[output[1]]*100 + foo[output[2]]*10 + foo[output[3]])

    return sum(four_digits)

print(part_two(data))
