from types import new_class


data = []

with open('day_14/input.txt') as file:
    for line in file:
        data.append(line.strip())

def part_one(data):
    polymer, rules = data[0], data[2:]
    rules = {rule.split(' -> ')[0]:rule.split(' -> ')[1] for rule in rules}

    for _ in range(10):
        pairs = [f"{polymer[i]}{polymer[i+1]}" for i in range(len(polymer)-1)]
        new_pairs = [*pairs]

        for pair, insertion in rules.items():
            if pair in pairs:
                indexes = [i for i,val in enumerate(new_pairs) if val == pair]
                for i in indexes:
                    new_pairs[i] = pair[0] + insertion + pair[1]

        polymer = new_pairs[0] + "".join(list(map(lambda x: x[1:], new_pairs[1:])))

    foo = {char: polymer.count(char) for char in polymer}
    a = max(foo.values())
    b = min(foo.values())

    return a - b

print(part_one(data))

from collections import defaultdict
def part_two(data):
    polymer, rules = data[0], data[2:]
    rules = {rule.split(' -> ')[0]:rule.split(' -> ')[1] for rule in rules}

    pairs = list(map(lambda x: "".join(x), zip(polymer, polymer[1:])))
    pairs = {pair: pairs.count(pair) for pair in pairs}
    letter_count = {char: polymer.count(char) for char in polymer}

    for _ in range(0, 40):
        new_pairs = {}

        for pair in pairs:
            if pair in rules:
                insertion = rules[pair]

                first_pair = pair[0] + insertion
                second_pair = insertion + pair[1]

                new_pairs[first_pair] = new_pairs.get(first_pair, 0) + pairs[pair]
                new_pairs[second_pair] = new_pairs.get(second_pair, 0) + pairs[pair]

                letter_count[insertion] = letter_count.get(insertion, 0) + pairs[pair]
            else:
                new_pairs[pair] = pairs[pair]

        pairs = new_pairs

    a = max(letter_count.values())
    b = min(letter_count.values())

    return a - b


print(part_two(data))
