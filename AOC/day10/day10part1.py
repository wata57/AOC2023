def checkUP(current):
  if pipe_map[(current[0] - 1, current[1])] in '|7FS':
    current = (current[0] - 1, current[1])
    return current
  return current
        
def checkLEFT(current):
  if pipe_map[(current[0], current[1] - 1)] in '-LFS':
    current = (current[0], current[1] - 1)
    return current
  return current

def checkRIGHT(current):
  if pipe_map[(current[0], current[1] + 1)] in '-J7S':
    current = (current[0], current[1] + 1)
    return current
  return current

def checkDOWN(current):
  if pipe_map[(current[0] + 1, current[1])] in '|JLS':
      current = (current[0] + 1, current[1])
      return current
  return current
    

with open('test.txt', 'r') as file:
  data = (file.read()).strip().split('\n')

points = []
pipe_map = {}

line_length = len(data[0])
data_length = len(data)

for r in range(line_length):
  for c in range(data_length):
    pipe_map[(r, c)] = data[r][c]
    if data[r][c] == 'S':
      s = (r, c)

start_points = []
current = s

# First start point(up)
if current[0] > 0 and checkUP(current) != current:
  n1 = checkUP(current)
  start_points.append(n1)
# Second start point(down)
if current[0] < data_length - 1 and checkDOWN(current) != current:
  n2 = checkDOWN(current)
  start_points.append(n2)
# Third start point(left)
if current[1] > 0 and checkLEFT(current) != current:
  n3 = checkLEFT(current)
  start_points.append(n3)
# Fourth start point(right)
if current[1] < line_length - 1 and checkRIGHT(current) != current:
  n4 = checkRIGHT(current)
  start_points.append(n4)

for start_point in start_points:
  route = {s}
  current = start_point
  while pipe_map[current] != 'S':
    if pipe_map[current] in '|LJS' and checkUP(current) not in route:
      route.add(current)
      current = checkUP(current)
    elif pipe_map[current] in '-J7S' and checkLEFT(current) not in route:
      route.add(current)
      current = checkLEFT(current)
    elif pipe_map[current] in '|F7S' and checkDOWN(current) not in route:
      route.add(current)
      current = checkDOWN(current)
    elif pipe_map[current] in '-FLS' and checkRIGHT(current) not in route:
      route.add(current)
      current = checkRIGHT(current)
    if s in route:
      route.remove(s)
  print(len(route))

print((len(route) + 1)//2)