# initializing list for input
input = list()

# opening input.txt
with open("input.txt", "r") as f:
    for line in f:
        input.append(line.rstrip())

