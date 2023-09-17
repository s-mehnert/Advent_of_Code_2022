#***** ADVENT OF CODE 2022 *****
#************ DAY 2 ************
#****************** Part 1 *****


imported_data = list()

with open("02_rock_paper_scissors_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n"))

print(imported_data)

scores = {"X" : 1, "Y" : 2, "Z" : 3, "won" : 6, "draw" : 3, "lost" : 0}
total_points = 0

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




    
