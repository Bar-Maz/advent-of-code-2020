def get_nth_number(input, goal):
    age = {}
    # initialize current number
    current_number = 0
    turn = 1
    for x in input:
        # hold 2 latest occurences of a given number
        age[x] = [turn, 0]
        current_number = x
        #increment turns
        turn += 1
    # all input numbers are unique, so the current number after initialization will be 0
    current_number = 0
    for turn in range(len(input)+1, goal):
        if current_number in age:
            # if current number is already in age object, mark current turn as hist latest occurrence
            age[current_number][1] = age[current_number][0]
            age[current_number][0] = turn
            # current numbers is a difference between last two turns with this number
            current_number = age[current_number][0] - age[current_number][1]
        else:
            # if its a new number, mark it as seen and set current number to 0
            age[current_number] = [turn, 0]
            current_number = 0
    return current_number


input = [18, 8, 0, 5, 4, 1, 20]
print("PART 1: ", get_nth_number(input, 2020))
print("PART 2: ", get_nth_number(input, 30000000))
