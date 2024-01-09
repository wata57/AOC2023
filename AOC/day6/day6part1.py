def travel_distance(speed, totalTime):
    return speed * (totalTime - speed)

with open('input.txt', 'r') as file:
    data = file.read()
    x = data.strip().split('\n')

b = [int(word) for word in (x[0].split(':'))[1].split(' ') if word != '']

d = [int(word) for word in (x[1].split(':'))[1].split(' ') if word != '']

time_distance = {}

result = 1

for i in range(len(b)):
    time_distance[b[i]] = d[i]

for key in time_distance:
    distances = []
    for i in range(key):
        d = travel_distance(i, key)
        if d > time_distance[key]:
            distances.append(d)
    print(distances)
    result *= len(distances)

print(result)