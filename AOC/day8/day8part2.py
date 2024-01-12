import math

with open('input.txt', 'r') as file:
    x, y = (file.read()).strip().split('\n\n')

# Create list to store all instructions in 0(left) or 1(right)
instr = [1 if char == 'R' else 0 for char in x]

# Turning data into a dictionary
netmap = {}

for line in y.split('\n'):
    a, b = line.split(' = ')
    netmap[a] = (b.replace("(", "").replace(")", "")).split(', ')

# Identifying all sequences that ends with 'A'
spots = [key for key in netmap if key[-1] == 'A']

count = 0
i = 0
c = 1
numbers = []
result = []

for x in spots:
    temp = []
    while True:
        # Return to first instruction after reaching the last one
        if i == len(instr):
            i = 0
        # Choose right or left based on the instructions list
        n = instr[i]
        # if last char is Z, append the count to the list 'numbers'
        if (netmap[x][n])[-1] == 'Z':
            # c equal to the number of steps it takes to reach a sequence that ends with 'Z'
            numbers.append(c)
            # Reset the count and return to first instruction before starting new sequence
            c = 1
            i = 0
            break
        else:
            # if last char isn't 'Z', choose right or left and move to next one
            c += 1
            i += 1
            x = netmap[x][n]

# Finding LCM of all c

result = math.lcm(numbers)
print(result)
