inputfile = open('trees.txt', 'r')



# Parse lines
data = [x.strip() for x in inputfile.readlines()]




def part1(data):
    x = 0                             # X is current column
    total = 0                         # Count of trees
    map_width = len(data[0])
    map_height = len(data)
    for y in range(map_height):       # Iterate each row
        if data[y][x] == '#':         # Use x,y as coordinates to check for tree
            total += 1                # Count if tree
        x = (x + 3) % map_width       # Jump 3 steps right (modulus to keep within map)
    return total



def part2(data):
    def traverse(right, down):              # Define a function for generalizing
        x = 0
        total = 0
        for i in range(len(data)):
            if i % down != 0:               # Skip rows according to "down"-variable
                continue
            if data[i][x] == '#':
                total += 1
            x = (x + right) % len(data[0])  # Use right-parameter
        return total

    # Use function to get values for each slope
    return traverse(1,1) * traverse(3,1) * traverse(5,1) * traverse(7,1) * traverse(1,2)

print(part2(data))