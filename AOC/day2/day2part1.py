def is_valid(item):
    for cubes in item:
        if int(cubes[0]) > int(rules[cubes[1]]):
            return False
    return True


rules = {
    'red': 12,
    'green': 13,
    'blue': 14
}

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
        if is_valid(item):
            game = int((x[0].split(' '))[1])
            res += game

    print(res)