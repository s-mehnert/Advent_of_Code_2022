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
files = dict()
visited = list()
current_dir = ""


for line in imported_data:
    if line.startswith("$"):
        command = line[2:4]
        if command == "cd":
            dir = line[5:]
            if dir == "..":
                visited.pop()
                current_dir = visited[-1]
                print("...moving up...")
            else:
                visited.append(dir)
                current_dir = dir
                if dir not in directories:
                    directories[dir] = list()
            print("current directory:", current_dir)
        elif command == "ls":
            continue
    elif line.startswith("dir"):
        child_dir = line[4:]
        if child_dir not in directories[current_dir]:
            directories[current_dir].append(child_dir)
            

print(directories)

    