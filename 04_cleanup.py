#***** ADVENT OF CODE 2022 *****
#************ DAY 4 ************
#****************** Part 1 *****


imported_data = list()

with open("04_cleanup_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n").split(","))


def format_section_list(elf_pairs):
    return [[[int(section) for section in elf.split("-")] for elf in pair] for pair in elf_pairs]

def find_complete_overlaps(elf_pairs):
    overlap_count = 0
    for pair in elf_pairs:
        elf_1_sections = [i for i in range(pair[0][0], pair[0][1]+1)]
        elf_2_sections = [i for i in range(pair[1][0], pair[1][1]+1)]
        if all(section in elf_1_sections for section in elf_2_sections) or all(section in elf_2_sections for section in elf_1_sections):
            overlap_count += 1
    return overlap_count


section_assignment = format_section_list(imported_data) 

print(f"There are {find_complete_overlaps(section_assignment)} elf pairs that have a complete overlap of sections.")


#****************** Part 2 *****

def find_any_overlap(elf_pairs):
    overlap_count = 0
    for pair in elf_pairs:
        elf_1_sections = [i for i in range(pair[0][0], pair[0][1]+1)]
        elf_2_sections = [i for i in range(pair[1][0], pair[1][1]+1)]
        for section in elf_1_sections:
            if section in elf_2_sections:
                overlap_count += 1
                break
    return overlap_count

print(f"There are {find_any_overlap(section_assignment)} elf pairs that have at least a partial overlap of sections.")
