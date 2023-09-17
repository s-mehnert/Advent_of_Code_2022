#***** ADVENT OF CODE 2022 *****
#************ DAY 1 *************
#****************** Part 1 *****

imported_data = list()

with open("1_elves_calories_input.txt") as input:
    cals_per_elf = 0
    for line in input.readlines():
        if line == "\n":
            imported_data.append(cals_per_elf)
            cals_per_elf = 0
        else:
            cals_per_elf += int(line.strip("\n"))
    imported_data.append(cals_per_elf)


max_cal_elf = max(imported_data)

print(f"The elf carrying the most calories is carrying {max_cal_elf} calories.")


#****************** Part 2 *****

max_cal_top_three_elves = sum(sorted(imported_data, reverse=True)[:3])

print(f"The top three elves carry {max_cal_top_three_elves} calories in total.")