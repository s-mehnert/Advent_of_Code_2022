#***** ADVENT OF CODE 2022 *****
#************ DAY 3 ************
#****************** Part 1 *****

imported_data = list()

with open("03_rucksack_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n"))


def find_faulty_item(rucksack):
    for char in rucksack[:len(rucksack)//2]:
        if char in rucksack[len(rucksack)//2:]:
            return char

# letters in string starting with * so that index can directly be used as corresponding value
letters = "*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

faulty_characters = list()

for rucksack in imported_data:
    faulty_characters.append(find_faulty_item(rucksack))

print(f"The priorities of the faulty items in all rucksacks together is {sum([letters.index(char) for char in faulty_characters])}.")


#****************** Part 2 *****

def find_badge(rucksack_group):
    for char in rucksack_group[0]:
        if char in rucksack_group[1] and char in rucksack_group[2]:
            return char

def split_list_in_groups(elves):
    return [elves[i:i+3] for i in range(0, len(elves), 3)]

badges = list()

for group in split_list_in_groups(imported_data):
    badges.append(find_badge(group))

print(f"The priorities of the badges all together is {sum([letters.index(badge) for badge in badges])}.")
