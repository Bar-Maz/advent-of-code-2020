# parse the input
def get_seats(lines):
    seats = []
    for line in lines:
        # 0 for '.', 1 for L
        seats.append([(char == 'L') - 1 for char in line])
    return seats

# get cell value while counting neighbors


def get_val(row, col, seats):
    max_row = len(seats) - 1
    max_col = len(seats[0]) - 1
    # check for index out of range
    if row > max_row or row < 0 or col > max_col or col < 0:
        return 0
    else:
        return seats[row][col] > 0

# count occupied seats near the current seat


def get_neighbors(row, col, seats):
    count = 0
    for c in range(col-1, col+2):
        for r in range(row-1, row+2):
            # don't count current seat
            if not (r == row and c == col):
                count += get_val(r, c, seats)
    return count

# count occupied seat seen from the current seat


def get_far_neighbors(row, col, seats):
    max_row = len(seats) - 1
    max_col = len(seats[0]) - 1
    # define 8 directions: horizontal, vertical and diagonals
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]
    count = 0
    for d in directions:
        # make one step in the given direction
        r, c = (row+d[0], col+d[1])
        # check if you're still in range
        if r > max_row or r < 0 or c > max_col or c < 0:
            val = 0
        else:
            val = seats[r][c]
            while val == -1:
                r += d[0]
                c += d[1]
                if r > max_row or r < 0 or c > max_col or c < 0:
                    val = 0
                else:
                    val = seats[r][c]
        # if val =/= -1, you are out of bound or you've found a seat, count it
        count += val > 0
    return count


def generate_new_seats(seats, far=False):
    new_seats = []
    # we stop the calculations when there's no changes
    modified = False
    for r, row in enumerate(seats):
        # initialize row
        new_seats.append([])
        for c, seat in enumerate(row):
            # don't try to change empty spaces
            if seat != -1:
                # depending on far (part 1 or part 2) argument, count nearest neighbors or the ones that you see
                neighbors_count = get_far_neighbors(
                    r, c, seats) if far else get_neighbors(r, c, seats)
                if seat:
                    # part 1: 4+, part 2: 5+; 3 + True = 4
                    if neighbors_count > 3 + far:
                        new_seats[r].append(0)
                        modified = True
                    else:
                        new_seats[r].append(1)
                else:
                    if not neighbors_count:
                        new_seats[r].append(1)
                        modified = True
                    else:
                        new_seats[r].append(0)
            else:
                new_seats[r].append(-1)
    return (new_seats, modified)


def stabilize(seats, far=False):
    modified = True
    while modified:
        seats, modified = generate_new_seats(seats, far)
    return seats


def part_1(lines):
    seats = stabilize(get_seats(lines))
    count = 0
    for row in seats:
        for seat in row:
            count += seat == 1
    return count


def part_2(lines):
    seats = stabilize(get_seats(lines), True)
    count = 0
    for row in seats:
        for seat in row:
            count += seat == 1
    return count


with open("input.txt", 'r') as input_file:
    lines = input_file.read().splitlines()
    print("PART 1: ", part_1(lines))
    print("PART 2: ", part_2(lines))
