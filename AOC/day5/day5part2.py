def conversion(numbers, maps):
    result = []
    for n in numbers:
        for line in maps:
            d,s,r = line.split(' ')
            if int(s) <= int(n) <= int(s) + int(r) - 1:
                    i = int(n) - int(s) + int(d)
                    result.append(i)
                    break
        else:
            result.append(int(n))
    return result

def maps(n):
    maP = s[n].split('\n')
    maP.pop(0)
    return maP

with open('input.txt', 'r') as file:
    data = file.read()
    s = data.strip().split('\n\n')

# SEEDS
title, seeds_numbers = s[0].split(': ')
seeds = seeds_numbers.split(' ')

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

print(min(location_numbers))