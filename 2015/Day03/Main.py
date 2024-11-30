# reading input.txt
file = open("input.txt").read()

# setting starting position of Santa
north_south = 0
east_west = 0

# initializing empty list
visited = []

# going through each character of file
for i in range(len(file)):

    # check if house was already visited, if not add it to visited list
    if (str(east_west) + ";" + str(north_south) not in visited):
        visited.append(str(east_west) + ";" + str(north_south))

    # following instructions and writing them to individual coordinates
    match(file[i]):
        case ">":
            east_west += 1
        case "<":
            east_west -= 1
        case "^":
            north_south += 1
        case "v":
            north_south -= 1

# printing result
print(len(visited))