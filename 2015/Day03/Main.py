# reading input.txt
file = open("input.txt").read()

# setting starting position of Santa
north_south = 0
east_west = 0

# setting starting position of Santa
r_north_south = 0
r_east_west = 0

# initializing coordinates
coords = 0
r_coords = 0

# initializing empty list
visited = []

# going through each character of file
for i in range(len(file)):

    if i % 2 == 0:
        # following instructions and writing them to individual coordinates
        match (file[i]):
            case ">":
                east_west += 1
            case "<":
                east_west -= 1
            case "^":
                north_south += 1
            case "v":
                north_south -= 1

        coords = str(east_west) + ";" + str(north_south)

        # check if house was already visited, if not add it to visited list
        if coords not in visited or r_coords not in visited:
            visited.append(coords)

    if i % 2 != 0:
        # following instructions and writing them to individual coordinates
        match (file[i]):
            case ">":
                r_east_west += 1
            case "<":
                r_east_west -= 1
            case "^":
                r_north_south += 1
            case "v":
                r_north_south -= 1

        r_coords = str(r_east_west) + ";" + str(r_north_south)

        # check if house was already visited, if not add it to visited list
        if coords not in visited or r_coords not in visited:
            visited.append(r_coords)

# printing result
print(len(visited))