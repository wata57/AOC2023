with open('input.txt', 'r') as file:
  data = list((file.read()).strip().split('\n'))

result = 0

for line in data:
  res = 0
  numbers = line.split(' ')
  all_lists = []
  sub_numbers = []
  i = 0
  x = numbers
  # c = len of previous list, starts with len(numbers) and decreases 1 after a new sub list is created
  c = len(numbers)
  while True:
    sub_numbers.append(int(x[i+1]) - int(x[i]))
    i += 1
    if len(sub_numbers) == c - 1:
      all_lists.append(sub_numbers)
      if all(element == 0 for element in sub_numbers):
        break
      else:
        x = sub_numbers
        i = 0
        c -= 1
        sub_numbers = []
  for sub_list in all_lists:
    res += int(sub_list[-1])
  result += res + int(numbers[-1])

print(result)