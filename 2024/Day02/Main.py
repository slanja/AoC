# initializing list for input
input = list()

# opening input.txt
with open("input.txt", "r") as f:
    for line in f:
        input.append(line.rstrip())

levels: list = list()

for line in input:
    numbers = line.split(" ")

    int_list = []

    for s in numbers:
        int_list.append(int(s))


    safe = True
    sf = all(int_list[i] <= int_list[i + 1] for i in range(len(int_list) - 1))
    sr = all(int_list[i] >= int_list[i + 1] for i in range(len(int_list) - 1))

    for i in range(len(int_list) - 1):

        if abs(int_list[i] - int_list[i + 1]) <= 3:
            if sf or sr:
                print(abs(int_list[i] - int_list[i + 1]))
                if abs(int_list[i] - int_list[i + 1]) != 0:
                    ...
                else:
                    safe = False
            else:
                safe = False
        else:
            safe = False

    print(int_list)
    print(safe, sf or sr)

    # 17 16 13 10 8 7 5
    # 8 11 13 14 17 18 21
    # 8 10 12 13 16 17 18 19

    if safe:
        levels.append(safe)

print(f"Safe levels:", sum(levels))
