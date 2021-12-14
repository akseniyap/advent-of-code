data = []                                                                       
                                                                                
with open('input.txt') as file:                                                 
    for line in file:                                                           
        data.append(line) 

data = data[0].strip().split(',')
data = list(map(int, data))


def part_one(data):
    for i in range(80):
        to_spawn = data.count(0)
        data = list(map(lambda x: x-1 if x != 0 else 6, data))
        if to_spawn:
            data += to_spawn * [8]

    return len(data)


print(part_one(data))


def part_two(data):
    initial = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
    set_vals = {el: data.count(el) for el in data}
    d = {**initial, **set_vals}
    d_copy = {**d}

    for i in range(256):
        spawn = d_copy[0]
        d_copy[7] = d[8]
        d_copy[6] = d[7] + d[0]
        d_copy[5] = d[6]
        d_copy[4] = d[5]
        d_copy[3] = d[4]
        d_copy[2] = d[3]
        d_copy[1] = d[2]
        d_copy[0] = d[1]
        d_copy[8] = spawn
        d = {**d_copy}

    return sum(d.values())


print(part_two(data))
