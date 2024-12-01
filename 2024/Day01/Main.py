# initializing list for input
input = list()

# opening input.txt
with open("input.txt", "r") as f:
    for line in f:
        input.append(line.rstrip())

# initializing empty lists
first_number = list()
second_number = list()

# creating variables for results
sum = 0
similarity = 0

# reading input line by line
for line in input:
    numbers = line.split("  ")
    first_number.append(int(numbers[0]))
    second_number.append(int(numbers[1]))

# sorting list for easier manipulation
first_number.sort()
second_number.sort()

# counting distance between two lists
for i in range(len(input)):
    if second_number[i] - first_number[i] >= 0:
        sum += second_number[i] - first_number[i]
    else:
        sum += first_number[i] - second_number[i]

#=== PART 2 ===
# counting how many times has number appeared in second_number list and multiplying it by first_number
for i in range(len(input)):
    similarity += first_number[i] * second_number.count(first_number[i])

# printing results
print("Total distance between lists: " + str(sum))
print("Similarity score: " + str(similarity))