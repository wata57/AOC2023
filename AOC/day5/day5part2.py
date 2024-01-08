def conversion(numbers, maps):
    result = []
    for n in numbers:
        for line in maps:
            s,d,r = line.split(' ')
            if int(s) <= int(n) <= int(s) + int(r) - 1:
                    i = int(n) - int(s) + int(d)
                    result.append(i)
                    break
        else:
            result.append(int(n))
    return result

with open('input.txt', 'r') as file:
    data = file.read()
    s = data.strip().split('\n\n')


# MAPS
# SEED TO SOIL
m1 = s[1].split('\n')
m1.pop(0)
# SOIL TO FERTILIZER
m2 = s[2].split('\n')
m2.pop(0)
# FERTILIZER TO WATER
m3 = s[3].split('\n')
m3.pop(0)
# WATER TO LIGHT
m4 = s[4].split('\n')
m4.pop(0)
# LIGHT TO TEMPERATURE
m5 = s[5].split('\n')
m5.pop(0)
# TEMPERATURE TO HUMIDITY
m6 = s[6].split('\n')
m6.pop(0)
#HUMIDITY TO LOCATION
m7 = s[7].split('\n')
m7.pop(0)

# LOCATION TO HUMIDITY
humidity_numbers = conversion(location_numbers, m7)

# HUMIDITY TO TEMPERATURE
temperature_numbers = conversion(humidity_numbers, m6)     

# TEMPERATURE TO LIGHT
light_numbers = conversion(temperature_numbers, m5)

# LIGHT TO WATER
water_numbers = conversion(light_numbers, m4)

# WATER TO FERTILIZER
fertilizer_numbers = conversion(water_numbers, m3)

# FERTILIZER TO SOIL
soil_numbers = conversion(fertilizer_numbers, m2)

# SOIL TO SEED
location_numbers = conversion(humidity_numbers, m7)

print(min(location_numbers))