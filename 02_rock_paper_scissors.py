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


    
