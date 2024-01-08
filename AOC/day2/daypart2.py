def is_valid(item):
    minimum = {}
    for cubes in item:
        minimum[cubes[1]] = max((minimum.get(cubes[1], 0)), int(cubes[0]))
    return minimum

res = 0

with open('input.txt', 'r') as file:
    for line in file:
        item = []
        x = line.split(':')
        y = x[1].split(';')
        for bag in y:
            n = bag.split(',')
            for _ in n:
                item.append(_.strip().split(' '))
            minimum = is_valid(item)
        res += minimum['red']*minimum['green']*minimum['blue']
    print(res)