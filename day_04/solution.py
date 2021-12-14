data = []                                                                       
                                                                                
with open('input.txt') as file:                                                 
    for line in file:                                                           
        data.append(line) 

data = list(map(lambda x: x.strip(), data))


def part_one(data):
    numbers = data[0].split(',')
    matrixes = data[1:]
    bingo = ['x', 'x', 'x', 'x', 'x']

    matrixes = [matrixes[i+1:i+6] for i in range(0, len(matrixes)-1, 6)]
    matrixes = [[row.split() for row in matrix] for matrix in matrixes]

    n = 0
    m = []
    for number in numbers:
        for matrix in matrixes:
            for row in matrix:
                if number in row:
                    index = row.index(number)
                    row[index] = 'x'

            transposed = [[el[i] for el in matrix] for i in range(5)]
            if any([el == bingo for el in matrix]) or any([el == bingo for el in transposed]):
                arr = [item for row in matrix for item in row if item != 'x']
                arr = list(map(lambda x: int(x),  arr))
                
                return sum(arr) * int(number)
                

print(part_one(data))


def part_two(data):
    numbers = data[0].split(',')
    matrixes = data[1:]
    bingo_matrixes = []
    bingo = ['x', 'x', 'x', 'x', 'x']

    matrixes = [matrixes[i+1:i+6] for i in range(0, len(matrixes)-1, 6)]
    matrixes = [[row.split() for row in matrix] for matrix in matrixes]
    
    for number in numbers:
        for matrix in matrixes:
            for row in matrix:
                if number in row:
                    index = row.index(number)
                    row[index] = 'x'

            # print(f"{number}: {matrixes}\n")
            transposed = [[el[i] for el in matrix] for i in range(5)]
            if any([el == bingo for el in matrix]) or any([el == bingo for el in transposed]):
#                print(bingo_matrixes)
                index = matrixes.index(matrix)
                if index not in bingo_matrixes:
                    bingo_matrixes.append(index)

                if len(matrixes) == len(bingo_matrixes):
                    m = matrixes[bingo_matrixes[-1]]
                    arr = [item for row in m for item in row if item != 'x']
                    arr = list(map(lambda x: int(x),  arr))

                    return sum(arr) * int(number)

#                    print(bingo_matrixes)
#                    print(matrixes[bingo_matrixes[-1]])
#                    print(number)
#                    return 


print(part_two(data))

