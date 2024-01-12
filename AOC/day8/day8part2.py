def is_correct(spots):
    for spot in spots:
        if spot[-1] != "Z":
            return False
    return True 

with open('input.txt', 'r') as file:
    x, y = (file.read()).strip().split('\n\n')

instr = [1 if char == 'R' else 0 for char in x]

netmap = {}

for line in y.split('\n'):
    a, b = line.split(' = ')
    netmap[a] = (b.replace("(", "").replace(")", "")).split(', ')

spots = []

for key in netmap:
    if key[-1] == 'A':
        spots.append(key)

i = 0
c = 0
result = []

print(spots)


while not is_correct(spots):
    if i == len(instr):
        i = 0
    new_spots = []
    n = instr[i]
    for spot in spots:
        new_spots.append(netmap[spot][n])
    spots = new_spots
    print(spots)
    c += 1
    i += 1
    if (spots[0])[-1] == 'Z':
        print(spots)
        break
print(c)
