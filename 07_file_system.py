# ***** ADVENT OF CODE 2022 *****
# ************ DAY 7 ************
# ****************** Part 1 *****

imported_data = list()

with open("07_file_system_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n"))

# for item in imported_data:
#     print(item)


directories = dict()
directory_sizes = dict()
path = list()
current_dir = ""


for line in imported_data:
    if line.startswith("$"):
        command = line[2:4]
        if command == "cd":
            dir = line[5:]
            if dir == "..":
                path.pop()
                current_dir = path[-1]
                print("...moving up...")
            else:
                path.append(dir)
                current_dir = dir
                if dir not in directories:
                    directories[dir] = [[], 0]
            print("current directory:", current_dir)
        elif command == "ls":
            continue
    elif line.startswith("dir"):
        child_dir = line[4:]
        if child_dir not in directories[current_dir][0]:
            directories[current_dir][0].append(child_dir)
    else:
        file_data = line.split()
        for dir in path:
            if dir not in directory_sizes:
                directory_sizes[dir] = int(file_data[0])
            else:
                directory_sizes[dir] += int(file_data[0])

print(directory_sizes)

total = 0
for key, value in directory_sizes.items():
    if value <= 100000:
        total += value

print(total)
