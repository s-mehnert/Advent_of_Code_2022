#***** ADVENT OF CODE 2022 *****
#************ DAY 2 ************
#****************** Part 1 *****


imported_data = list()

with open("02_rock_paper_scissors_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n"))


scores = {"X" : 1, "Y" : 2, "Z" : 3, "won" : 6, "draw" : 3, "lost" : 0}

def play_round(input):
    outcome = ""
    shape = input[2]
    if input[0] == "A":
        if shape == "X":
            outcome = "draw"
        elif shape == "Y":
            outcome = "won"
        elif shape == "Z":
            outcome = "lost"
    elif input[0] == "B":
        if shape == "X":
            outcome = "lost"
        elif shape == "Y":
            outcome = "draw"
        elif shape == "Z":
            outcome = "won"
    elif input[0] == "C":
        if shape == "X":
            outcome = "won"
        elif shape == "Y":
            outcome = "lost"
        elif shape == "Z":
            outcome = "draw"
    return outcome

def calculate_points(shape, outcome):
    return scores[shape] + scores[outcome]


total_points = 0
for round in imported_data:
    total_points += calculate_points(round[2], play_round(round))

    
print(f"The total score when following the strategy guide would be {total_points} points.")


#****************** Part 2 *****

def play_round_modified(input):
    outcome = input[2]
    shape = ""
    if input[0] == "A":
        if outcome == "X":
            shape = "Z"
        elif outcome == "Y":
            shape = "X"
        elif outcome == "Z":
            shape = "Y"
    elif input[0] == "B":
        if outcome == "X":
            shape = "X"
        elif outcome == "Y":
            shape = "Y"
        elif outcome == "Z":
            shape = "Z"
    elif input[0] == "C":
        if outcome == "X":
            shape = "Y"
        elif outcome == "Y":
            shape = "Z"
        elif outcome == "Z":
            shape = "X"
    return shape

def calculate_points_modified(shape, outcome):
    if outcome == "X":
        outcome = "lost"
    elif outcome == "Y":
        outcome = "draw"
    elif outcome == "Z":
        outcome = "won"
    return scores[shape] + scores[outcome]

