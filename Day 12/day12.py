# move in a given direction
def move(x_pos, y_pos, direction, distance):
    return {
        'E': (x_pos+distance, y_pos),
        'S': (x_pos, y_pos-distance),
        'W': (x_pos-distance, y_pos),
        'N': (x_pos, y_pos+distance),
    }.get(direction)

# rotate the ship right or left
def change_direction(current_dir, turn, value):
    return {
        'R': (current_dir+value//90) % 4,
        'L': (current_dir-value//90) % 4,
    }.get(turn)

# rotate the waypoint around the ship once clockwise
def rotate_once(wx, wy):
    return(wy, -wx)

# rotate the waypoint around the ship
def rotate_waypoint(wx, wy, turn, value):
    # set current waypoint
    x = wx
    y = wy
    # get amount of clockwise 90deg turns
    steps = {
        'R': (value//90),
        'L': ((360-value)//90) % 4,
    }.get(turn)
    # rotate the ship as much as you need
    for i in range(steps):
        x, y = rotate_once(x, y)
    return (x, y)

# move according to waypoint
def move_to_waypoint(x_pos, y_pos, wx, wy, value):
    return(x_pos + wx * value, y_pos + wy * value)


def part_1(lines):
    directions = ['E', 'S', 'W', 'N']
    turns = ['R', 'L']
    x_pos = 0
    y_pos = 0
    current_dir = 0
    for line in lines:
        direction = line[0]
        value = int(line[1:])
        if direction in directions:
            x_pos, y_pos = move(x_pos, y_pos, direction, value)
        elif direction in turns:
            current_dir = change_direction(current_dir, direction, value)
        else:
            x_pos, y_pos = move(x_pos, y_pos, directions[current_dir], value)
    return abs(x_pos) + abs(y_pos)


def part_2(lines):
    directions = ['E', 'S', 'W', 'N']
    turns = ['R', 'L']
    x_pos = 0
    y_pos = 0
    wx = 10
    wy = 1
    for line in lines:
        direction = line[0]
        value = int(line[1:])
        if direction in directions:
            wx, wy = move(wx, wy, direction, value)
        elif direction in turns:
            wx, wy = rotate_waypoint(wx, wy, direction, value)
        else:
            x_pos, y_pos = move_to_waypoint(x_pos, y_pos, wx, wy, value)
    return abs(x_pos) + abs(y_pos)


input_file = open("input.txt", 'r')
lines = input_file.read().splitlines()
print("PART 1: ", part_1(lines))
print("PART 2: ", part_2(lines))
