#***** ADVENT OF CODE 2022 *****
#************ DAY 5 ************
#****************** Part 1 *****

from collections import deque

imported_data = list()

with open("05_supply_input.txt") as input:
    bulk = input.read()
    imported_data = bulk.split("\n\n")


stacks_raw_data = imported_data[0].split("\n")
instructions = imported_data[1].split("\n")

stack_rows = list()
for row in stacks_raw_data:
    stack_rows.append([row[1], row[5], row[9]])
stack_rows.pop()
stack_rows.reverse()

def build_stacks(rows_bottom_up):
    stack_list = list()
    for i in range(len(rows_bottom_up[0])):
        stack_list.append(deque())
    for row in rows_bottom_up:
        for i in range(len(row)):
            if row[i] == " ":
                continue
            stack_list[i].append(row[i])
    return stack_list

initial_stacks = build_stacks(stack_rows)

formatted_instructions = list()

for row in instructions:
    instr = row.split()
    formatted_instructions.append([int(instr[1]), int(instr[3]), int(instr[5])])

print(formatted_instructions)

def move_item(stack_list, from_stack, to_stack):
    stack_list[to_stack-1].append(stack_list[from_stack-1].pop())
    return stack_list
print(initial_stacks)
print(move_item(initial_stacks, 1, 2))

def process_instructions(stacks, instruction):
    pass




#****************** Part 2 *****
