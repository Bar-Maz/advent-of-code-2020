def get_valid_ranges(lines):
    ranges = []
    for line in lines:
        split_by_colon = line.split(':')
        if len(split_by_colon) < 2:
            break
        new_ranges = [[int(i) for i in x.split('-')]
                      for x in split_by_colon[1].split('or')]
        for rng in new_ranges:
            ranges.append(rng)
    final_ranges = []
    for rng in ranges:
        new = True
        for fr in final_ranges:
            if rng[0] <= fr[0] and rng[1] <= fr[1] and rng[1] >= fr[0]:
                fr[0] = rng[0]
                new = False
            if rng[1] > fr[1] and rng[0] <= fr[1] and rng[0] >= fr[0]:
                fr[1] = rng[1]
                new = False
        if new:
            final_ranges.append(rng)
    return final_ranges


def get_ticket_values(lines):
    read = False
    ticket_values = []
    for line in lines:
        if read:
            for val in line.split(','):
                if val:
                    ticket_values.append(int(val))
            continue       
        if line == 'nearby tickets:':
            read = True
    return ticket_values

def part_1(lines):
    sum = 0
    ticket_values = get_ticket_values(lines)
    ranges = get_valid_ranges(lines)
    for val in ticket_values:
        ok = False
        for rng in ranges:
            if val>=rng[0] and val<=rng[1]:
                ok = True
                break
        if not ok:
            sum+=val           
    return sum

def part_2(lines):
    ...


input_file = open("input.txt", 'r')
lines = input_file.read().splitlines()
print("PART 1: ", part_1(lines))
print("PART 2: ", part_2(lines))
