data = []

with open('input.txt') as file:
    for line in file:
        data.append(line)

data = list(map(lambda x: x.strip(), data))

def transpose(matrix):
    cols = len(matrix)
    rows = len(matrix[0])
    result = [['' for _ in range(cols)] for _ in range(rows)]

    for i in range(cols):
        for j in range(rows):
            result[j][i] = matrix[i][j]

    return result

def part_one(data):
    coords, instructions = data[:data.index('')], data[data.index('')+1:]
    coords = [[int(coord) for coord in xy.split(',')] for xy in coords]

    instructions = [(instr[instr.index('=')-1], instr[instr.index('=')+1:]) for instr in instructions]

    cols = max([coord[0] for coord in coords])
    rows = max([coord[1] for coord in coords])
    board = [['.' for _ in range(cols+1)] for _ in range(rows+1)]

    for xy in coords:
        x, y = xy
        board[y][x] = '#'

    for instruction in instructions[0:1]:
        if instruction[0] == 'x':
            board = transpose(board)

        for row in range(int(instruction[1])):
            a = board[row]
            b = board[len(board)-1-row]

            board[row] = ['#' if '#' in (x, y) else '.' for x, y in zip(a, b)]

        for row in range(len(board)-int(instruction[1])):
            board.pop(-1)

        if instruction[0] == 'x':
            board = transpose(board)


    foo = [item for sublist in board for item in sublist].count('#')
    print(f"res: {foo}")


print(part_one(data))


def part_two(data):
    coords, instructions = data[:data.index('')], data[data.index('')+1:]
    coords = [[int(coord) for coord in xy.split(',')] for xy in coords]

    instructions = [(instr[instr.index('=')-1], instr[instr.index('=')+1:]) for instr in instructions]

    cols = max([coord[0] for coord in coords])
    rows = max([coord[1] for coord in coords])
    board = [['.' for _ in range(cols+1)] for _ in range(rows+1)]

    for xy in coords:
        x, y = xy
        board[y][x] = '#'

    for instruction in instructions:
        print(instruction)
        if instruction[0] == 'x':
            board = transpose(board)

        for row in range(int(instruction[1])):
            a = board[row]
            b = board[len(board)-1-row]

            board[row] = ['#' if '#' in (x, y) else '.' for x, y in zip(a, b)]

        for row in range(len(board)-int(instruction[1])):
            board.pop(-1)

        if instruction[0] == 'x':
            board = transpose(board)


    foo = [item for sublist in board for item in sublist].count('#')

    for line in board:
        print(line)
    print(f"res: {foo}")

print(part_two(data))
