from math import lcm

# get first timestamp with a given bus after a given timestamp


def get_next_bus(line, timestamp):
    return (line - ((timestamp + line) % line), line)


def part_1(timestamp, lines_str):
    # get all lines that aren't marked as x
    lines = [int(nr)
             for nr in lines_str.split(',') if not nr == 'x']
    # make 1st one the best bus to take at the moment
    best_bus = get_next_bus(lines[0], timestamp)
    # check other lines
    for line in lines[1:]:
        bus = get_next_bus(line, timestamp)
        # if you wait less than the best bus, that's the new best bus
        if bus[0] < best_bus[0]:
            best_bus = bus
    return best_bus[0] * best_bus[1]


def part_2(lines_str):
    lines = {}
    # get lines {offset1: line1, offset2: line2, ...}
    for idx, nr in enumerate(lines_str.split(',')):
        if not nr == 'x':
            max_offset = idx
            lines[idx] = int(nr)
    # we'll be incrementing by the times between first line at the beginning
    increment = lines[0]
    # initialize the first timestamp that works for both busses
    first_cross = lines[0]
    for offset in lines:
        # skip the first line
        if not offset:
            continue
        # begin with last working crossover point
        timestamp = first_cross
        # reset the first common timestamp
        first_cross = 0
        # while it's zero, increment the timestamp
        while (not first_cross):
            # if you found the timestamp that works for two busses + offset, save it and go for another bus
            # example: we begin with timestamp = 0, increment by 7, offset is equal to 1 and our current line is 13
            # we go through each 7n+1 (n - increment) and check if its divisible by 13, the first one we find is 77 + 1
            # we save 77 as our starting point and set increment to smallest multiply of both 13 and 7 - 91
            # we do this because we know that these busses will align in the same way each 91 minutes
            # trying to increment two timestamps by 7 and 13 and then checking these works for small numbers, but it took too long
            # for the my input. We start from 77 and build our way up by 91 each step, checking each value by adding offset and dividing
            #  by next line interval. The first common timestamp with the last line is the answer.
            if not (timestamp + offset) % lines[offset]:
                first_cross = timestamp
                if max_offset == offset:
                    return first_cross
                increment = lcm(lines[offset], increment)
            timestamp += increment


with open("input.txt", 'r') as input_file:
    timestamp = int(input_file.readline())
    lines_str = input_file.readline()
    print("PART 1: ", part_1(timestamp, lines_str))
    print("PART 2: ", part_2(lines_str))
