#***** ADVENT OF CODE 2022 *****
#************ DAY 5 ************
#****************** Part 1 *****

from collections import deque

imported_data = list()

with open("05_supply_input.txt") as input:
    bulk = input.read()
    imported_data = bulk.split("\n\n")


stacks_raw_data = imported_data[0].split("\n")
stack_rows = list()

for row in stacks_raw_data:
    items = list()
    for i in range(1, len(row)-1, 4):
        items.append(row[i])
    stack_rows.append(items)
stack_rows.pop()
stack_rows.reverse()

instructions = imported_data[1].split("\n")
formatted_instructions = list()

for row in instructions:
    instr = row.split()
    formatted_instructions.append([int(instr[1]), int(instr[3]), int(instr[5])])


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

def move_item(stack_list, from_stack, to_stack):
    stack_list[to_stack-1].append(stack_list[from_stack-1].pop())
    return stack_list

def process_instructions(stacks, instructions):
    for instruction in instructions:
        for i in range(instruction[0]):
            move_item(stacks, instruction[1], instruction[2])
    return stacks

def decipher_message(stacks):
    message = ""
    for stack in stacks:
        message += stack[-1]
    return message


initial_stacks = build_stacks(stack_rows)
stacks_after_rearrangement = process_instructions(initial_stacks, formatted_instructions)

print(f"The message is {decipher_message(stacks_after_rearrangement)}.")



#****************** Part 2 *****
