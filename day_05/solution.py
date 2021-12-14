data = []                                                                       
                                                                                
with open('input.txt') as file:                                                 
    for line in file:                                                           
        data.append(line) 

s = 1000
data = list(map(lambda x: x.strip().split(' -> '), data))


def part_one(data):
    area = [s * [0] for i in range(s)]

    for coordinates in data:
        start, end = list(map(lambda x: x.split(','), coordinates))
        start = list(map(int, start))
        end = list(map(int, end))
 
        if start[0] == end[0]:
            y = start[0]
            r = []
            if start[1] < end[1]:
                r = range(start[1], end[1]+1)
            else:
                r = range(end[1], start[1]+1)

            for i in r:
                area[y][i] += 1
 
        if start[1] == end[1]:
            x = start[1]
            r = []
            if start[0] < end[0]:
                r = range(start[0], end[0]+1)
            else:
                r = range(end[0], start[0]+1)

            for i in r:
                area[i][x] += 1
    a = [item for sublist in area for item in sublist]
    return len(a) - a.count(0) - a.count(1)
    

print(part_one(data))

# x, y -> x, y
# 9, 7 -> 7, 9
def part_two(data):
    area = [s * [0] for i in range(s)]

    for coordinates in data:
        start, end = list(map(lambda x: x.split(','), coordinates))
        start = list(map(int, start))
        end = list(map(int, end))
 
        # same x
        if start[0] == end[0]:
            x = start[0]
            r = []
            if start[1] < end[1]:
                r = range(start[1], end[1]+1)
            else:
                r = range(end[1], start[1]+1)

            for i in r:
                area[i][x] += 1
 
        elif start[1] == end[1]:
            y = start[1]
            r = []
            if start[0] < end[0]:
                r = range(start[0], end[0]+1)
            else:
                r = range(end[0], start[0]+1)

            for i in r:
                area[y][i] += 1
    
        else:
            r = range(0, abs(start[0] - end[0]) + 1)
            for i in r:
                if start[0] > end[0]:
                    if start[1] > end[1]:
                        # x--, y--
                        area[start[1]-i][start[0]-i] += 1
                    else:
                        # x--, y++
                        area[start[1]+i][start[0]-i] += 1
                else:
                    if start[1] > end[1]:
                        # x++, y--
                        area[start[1]-i][start[0]+i] += 1
                    else:
                        # x++, y++
                        area[start[1]+i][start[0]+i] += 1

    a = [item for sublist in area for item in sublist]
    return len(a) - a.count(0) - a.count(1)


print(part_two(data))
