# reading input.txt
file = open("input.txt").readlines()

paper = 0
ribbon = 0

for line in file:
    dimensions = line.split("x")

    # converting string list to int list
    dimensions = [int(item) for item in dimensions]

    # getting dimensions of every present
    length = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]

    # sorting dimensions, so I can get smallest sides
    dimensions.sort()

    # calculating area of smallest side
    extra = dimensions[0] * dimensions[1]

    # calculating ribbon to wrap present
    wrap = dimensions[0]*2 + dimensions[1]*2

    # calculating ribbon for the bow
    bow = dimensions[0] * dimensions[1] * dimensions[2]


    ribbon += wrap + bow

    # calculation total area of wrapping paper needed
    paper += (2 * length * width + 2 * width * height + 2 * height * length) + extra


print("Paper: " + str(paper))
print("Ribbon: " + str(ribbon))