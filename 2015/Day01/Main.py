# reading input.txt
file = open('.venv/input.txt').read()

# setting starting position of Santa
floor = 0

# going through each character
for i in range(len(file)):
    # checking if Santa reached -1 floor
    if (floor == -1):
        print(i)
    # checking and following instructions
    match(file[i]):
        case "(":
            floor += 1
        case ")":
            floor -= 1

print("Floor: " + str(floor))