with open('input.txt', 'r') as file:
    data = file.read()
    s = data.strip().split('\n')
result = 0
for line in s:
    numbers = [char for char in line if char.isdigit()]
    result += int(numbers[0] + numbers[-1])
print(result)