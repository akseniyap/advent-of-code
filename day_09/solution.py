data = []

with open('day_09/input.txt') as file:
    for line in file:
        data.append(line)

data = list(map(lambda x: list(x.strip()), data))
data = [[int(x) for x in line] for line in data]

low_points = []
def part_one(data):
    rows = len(data)
    cols = len(data[0])
    risk_levels = 0
    global low_points

    for i in range(rows):
        for j in range(cols):
            el = data[i][j]

            if (i-1) >= 0:
                up = data[i-1][j]
            else:
                up = None
            if (i+1) < rows:
                down = data[i+1][j]
            else:
                down = None
            if (j-1) >= 0:
                left = data[i][j-1]
            else:
                left = None
            if (j+1) < cols:
                right = data[i][j+1]
            else:
                right = None

            adjacents = [ad for ad in (up, down, left, right) if ad != None]
            if all(map(lambda ad: ad > el, adjacents)):
                low_points.append([i, j])
                risk_levels += (el + 1)

    return risk_levels

print(part_one(data))

def basin_size(data, x, y):
    basin = {(x, y)}
    checked = []

    rows = len(data)
    cols = len(data[0])

    def search_basin(x, y):
        to_search = []
        nonlocal basin, checked
                    #   up      down     left    right
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        if (x, y) in checked:
            return

        for x_direction, y_direction in directions:
            x_offset = x + x_direction
            y_offset = y + y_direction

            point = data[x][y]
            if rows > x_offset >= 0 and cols > y_offset >= 0:
                adjacent = data[x_offset][y_offset]
            else:
                continue

            while adjacent and point < adjacent < 9:
                adjacent_coords = (x_offset, y_offset)
                basin.add(adjacent_coords)

                if adjacent_coords not in checked:
                    to_search.append(adjacent_coords)

                point = data[x_offset][y_offset]
                x_offset += x_direction
                y_offset += y_direction

                if rows > x_offset >= 0 and cols > y_offset >= 0:
                    adjacent = data[x_offset][y_offset]
                else:
                    adjacent = None

            checked.append((x, y))

            for foo in to_search:
                search_basin(*foo)

    search_basin(x, y)
    return len(basin)

def part_two(data):
    global low_points

    basin_sizes = {}

    for point in low_points:
        foo = basin_size(data, *point)
        basin_sizes["-".join(map(str, point))] = foo

    a, b, c = sorted(basin_sizes.values())[-3:]

    return a * b * c

print(part_two(data))
