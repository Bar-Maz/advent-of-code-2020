def get_named_validators(lines):
    # validators are located at the begginning so we can just read them until we get a line without a colon
    # then we split it by colon, getting name and ranged, we split ranges by or, and then
    # we split individual numbers by dashes
    validators = {}
    for line in lines:
        split_by_colon = line.split(':')
        if len(split_by_colon) < 2:
            break
        validators[split_by_colon[0].strip()] = [[int(i) for i in x.split('-')]
                                                 for x in split_by_colon[1].split('or')]
    return validators


def get_valid_ranges(lines):
    # I thought that maybe it will come in handy in part 2 or sth, but this generally reduces
    # number of ranges required to check by A LOT.
    # ranges 1-3, 5-7, 6-9 are reduced to 1-3, 5-9
    ranges = []
    validators = get_named_validators(lines)
    for val in validators.values():
        for rng in val:
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


def get_tickets(lines):
    # getting all nearby tickets
    # read file until you find a line that says nearby tickets and then just get all lines splitting them by ,
    read = False
    tickets = []
    for line in lines:
        if read:
            tickets.append([int(val) for val in line.split(',')])
            continue
        if line == 'nearby tickets:':
            read = True
    return tickets


def get_my_ticket(lines):
    # get my ticket by reading lines until you get your ticket, then read the next line and split by ,
    read = False
    tickets = []
    for line in lines:
        if read:
            return [int(val) for val in line.split(',')]
        if line == 'your ticket:':
            read = True
    return tickets


def get_ticket_values(lines):
    # get all ticket values in one array
    # nested list comprehension: [val for ticket in tickets for val in tickets] -
    # val in tickets gets executed before val for ticket
    tickets = get_tickets(lines)
    ticket_values = [val for ticket in tickets for val in ticket]
    return ticket_values


def validate(validators, value):
    # given a dict of valid ranges and a value, get all keys that don't match the value
    bad = []
    for key, ranges in validators.items():
        valid = False
        for rng in ranges:
            if value >= rng[0] and value <= rng[1]:
                valid = True
                break
        if not valid:
            bad.append(key)
    return bad


def part_1(lines):
    # get all tickets, get all ranges, check each value for all ranges, multiply the bad ones
    sum = 0
    ticket_values = get_ticket_values(lines)
    ranges = get_valid_ranges(lines)
    for val in ticket_values:
        ok = False
        for rng in ranges:
            if val >= rng[0] and val <= rng[1]:
                ok = True
                break
        if not ok:
            sum += val
    return sum


def part_2(lines):
    # get validators by name and all tickets
    validators = get_named_validators(lines)
    validators_count = len(validators)
    tickets = get_tickets(lines)
    # validate the tickets
    # the output is a list of lists of lists xD
    # lists of bad values of each val of each ticket
    validated = [[validate(validators, val) for val in ticket]
                 for ticket in tickets]
    # get only the valid tickets
    # if ticket has all validators listed in one of its arrays,
    # it's invalid because the value didn't match any of the values
    valid = []
    for ticket in validated:
        ok = True
        for val in ticket:
            if len(val) == validators_count:
                ok = False
        if ok:
            valid.append(ticket)
    # get all possible indexes for each index of a single ticket
    # iterate over values in tickets and eliminate its index
    # from a set of possible indexes of each parameter
    # if you have sth like:
    # 'wagon': {0,1,2,3,4}
    # and ticket looks like: [[],[],[],['wagon],[]]
    # you're left with 'wagon':{0,1,2,4}
    possible_indexes = {}
    for key in validators:
        possible_indexes[key] = set(range(validators_count))
    for ticket in valid:
        for idx, val in enumerate(ticket):
            if val:
                for name in val:
                    possible_indexes[name].discard(idx)
    # sort possible indexes by set length
    # each next set has 1,2,3,4,5,6... elements
    sorted_indexes = {k: v for k, v in sorted(
        possible_indexes.items(), key=lambda item: len(item[1]))}
    indexes = {}
    # get first value from indexes, it has length 1
    # set the value as it's real index, and discard the index from all the other sets
    # next entry will lose this index and you're left with only one index
    # repeat for all parameters
    for k, v in sorted_indexes.items():
        val = list(v)[0]
        indexes[k] = val
        for x in sorted_indexes.values():
            x.discard(val)
    # get my ticket and multiply every entry that begins with departure
    my_ticket = get_my_ticket(lines)
    result = 1
    for k, v in indexes.items():
        if k.find("departure") == 0:
            result *= my_ticket[v]
    return result


with open("input.txt", 'r') as input_file:
    lines = input_file.read().splitlines()
    print("PART 1: ", part_1(lines))
    print("PART 2: ", part_2(lines))
