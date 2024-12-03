import re

def mul(x, y) -> int:
    return x * y

# initializing list for input
input = list()

# opening input.txt
with open("input.txt", "r") as f:
    for line in f:
        input.append(line.rstrip())

pattern = r"mul\((\d+),(\d+)\)"

# finding all parts that matches pattern
for line in input:
    matches = re.findall(pattern, line)

result = 0

# multiplication of every set numbers, that was found
for i in range(len(matches)):
    x, y = int(matches[i][0]), int(matches[i][1])
    result += mul(x, y)

print("Result:",result)