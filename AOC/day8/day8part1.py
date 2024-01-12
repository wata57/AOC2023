with open('input.txt', 'r') as file:
    x, y = (file.read()).strip().split('\n\n')

# Create list to store all instructions in 0(left) or 1(right)
instr = [1 if char == 'R' else 0 for char in x]


# Turning data into a dictionary
netmap = {}

for line in y.split('\n'):
    a, b = line.split(' = ')
    netmap[a] = (b.replace("(", "").replace(")", "")).split(', ')

result = 0
c = 1
i = 0
# Starting at 'AAA'
x = 'DJD'

while True:
    # Return to first instruction after reaching the last one
    if i == len(instr):
        i = 0
    # Choose right or left based on the instruction list
    n = instr[i]
    if netmap[x][n][-1] == 'Z':
        result = c
        break
    else:
        # if netmap[x][n] is not 'ZZZ', choose right or left and move to next one
        c += 1
        i += 1
        x = netmap[x][n]

print(result)