def travel_distance(speed, totalTime):
    return speed * (totalTime - speed)

time_distance = {49787980: 298118510661181}
result = 1

distances = []
for i in range(49787980):
    d = travel_distance(i, 49787980)
    if d > time_distance[49787980]:
        distances.append(d)
result *= len(distances)

print(result)
