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
