#***** ADVENT OF CODE 2022 *****
#************ DAY 4 ************
#****************** Part 1 *****


imported_data = list()

with open("04_cleanup_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n"))

print(imported_data)