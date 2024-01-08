def conversion(numbers, maps):
    result = []
    while len(numbers) > 0:
        a, b = numbers.pop()
        temp = []
        for line in maps:
            d, s, r = map(int, line.split(' '))
            if s <= a < s + r and b <= s + r:
                temp.append((a - s + d, b - s + d))
                break
            elif s > a and b > s + r:
                numbers.append((a, s - 1))
                temp.append((s - s + d, s + r - s + d))
                numbers.append((r + s + 1, b))
                break
            elif s > a and s <= b <= s + r:
                numbers.append((a, s - 1))
                temp.append((s - s + d, b - s + d))
                break
            elif s <= a < s + r and b > s + r:
                temp.append((a - s + d, s + r - s + d))
                numbers.append((s + r, b))
                break
        if len(temp) == 0:
            temp.append((a, b))
        result += temp
    return result

def maps(x):
    maP = parsed_data[x].split('\n')
    maP.pop(0)
    return maP

with open('input.txt', 'r') as file:
    data = file.read()
    parsed_data = data.strip().split('\n\n')

# SEEDS
title, seeds_numbers = parsed_data[0].split(': ')
seeds_range = seeds_numbers.split(' ')

i = 0
seeds = []
while i < len(seeds_range):
    x, y = map(int, (seeds_range[i], seeds_range[i+1]))
    seeds.append((x, x + y))
    i += 2

# SEED TO SOIL
soil_numbers = conversion(seeds, maps(1))

# SOIL TO FERTILIZER
fertilizer_numbers = conversion(soil_numbers, maps(2))     

# FERTILIZER TO WATER
water_numbers = conversion(fertilizer_numbers, maps(3))

# WATER TO LIGHT
light_numbers = conversion(water_numbers, maps(4))

# LIGHT TO TEMPERATURE
temperature_numbers = conversion(light_numbers, maps(5))

# TEMPERATURE TO HUMIDITY
humidity_numbers = conversion(temperature_numbers, maps(6))

# HUMIDITY TO LOCATION
location_numbers = conversion(humidity_numbers, maps(7))

print(min(location_numbers)[0])