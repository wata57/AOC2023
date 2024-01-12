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
  all_lists.append(list(map(int, numbers)))
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

  current = 0
  for sub_list in reversed(all_lists):
    current = sub_list[0] - current
  result += current
print(result)