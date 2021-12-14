data = []                                                                       
                                                                                
with open('input.txt') as file:                                                 
    for line in file:                                                           
        data.append(line)

data = list(map(lambda x: x.strip(), data))

def part_one(data):
    result = 0
    wrong_characters = []
    pairs = {'': '', ')': '(', ']': '[', '}': '{', '>': '<'}

    for line in data:
        stack = ['']

        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.insert(0, char)
            else:
                opening = pairs[char]
                if opening == stack[0]:
                    stack.pop(0)
                else:
                    wrong_characters.append(char)
                    break

    table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    foo = {el: wrong_characters.count(el) for el in wrong_characters}
    print(foo)
    for key, value in foo.items():
        result += (table[key] * value)

    return result

print(part_one(data))


def part_two(data):
    missing_characters = []
    pairs = {'': '', ')': '(', ']': '[', '}': '{', '>': '<'}

    for line in data:
        stack = ['']

        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.insert(0, char)
            else:
                opening = pairs[char]
                if opening == stack[0]:
                    stack.pop(0)
                else:
                    stack = []
                    break
        if stack:
            stack.pop(-1)
            missing_characters.append(stack)

    table = {'(': 1, '[': 2, '{': 3, '<': 4}
    foo = []
    for line in missing_characters:
        result = 0
        for item in line:
            result *= 5
            result += table[item]

        foo.append(result)

    foo = sorted(foo)
    return foo[int(len(foo)/2)]

print(part_two(data))
