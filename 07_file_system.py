# ***** ADVENT OF CODE 2022 *****
# ************ DAY 7 ************
# ****************** Part 1 *****

imported_data = list()

with open("07_file_system_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n"))

for item in imported_data:
    print(item)