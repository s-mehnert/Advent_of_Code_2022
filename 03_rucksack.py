imported_data = list()

with open("03_rucksack_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n"))

print(imported_data)