with open('input.txt', 'r') as file:
    x, y = (file.read()).strip().split('\n\n')

instr = [1 if char == 'R' else 0 for char in x]

netmap = {}
spots = []

for line in y.split('\n'):
    a, b = line.split(' = ')
    netmap[a] = (b.replace("(", "").replace(")", "")).split(', ')
    spots.append(a)


result = 0
c = 1
i = 0
x = 'AAA'

while True:
    if i == len(instr):
        i = 0
    n = instr[i]
    if netmap[x][n] == 'ZZZ':
        result = c
        break
    else:
        c += 1
        i += 1
        x = netmap[x][n]

print(result)