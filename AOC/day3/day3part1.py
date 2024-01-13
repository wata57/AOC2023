with open('input.txt', 'r') as file:
    data = file.read()
    s = data.strip().split('\n')

symbols = set(['@', '+', '&', '/', '*', '%', '$', '=', '#', '-'])
hms = {}
hm = {}
result = 0

for r in range(len(s)):
    for c in range(len(s[0])):
        if s[r][c] in symbols:
            hms[(r, (c))] = s[r][c]
        if s[r][c].isdigit():
            hm[(r, (c))] = s[r][c]
        if (r,c-1) in hm and s[r][c].isdigit():
            hm[(r,(c-1,c))] = s[r][c-1] + s[r][c]
            hm.pop((r,c))
            hm.pop((r,c-1))
        if (r,(c-2,c-1)) in hm and s[r][c].isdigit():
            hm[(r,(c-2,c-1,c))] = s[r][c-2] + s[r][c-1] + s[r][c]
            hm.pop((r,c))
            hm.pop((r,(c-2,c-1)))

for key in hm:
    # one digit number
    if len(hm[key]) == 1:   
        # LEFT OR RIGHT
        if (key[0], key[1] - 1) in hms:
            result += int(hm[key])
        elif (key[0], key[1] + 1) in hms:
            result += int(hm[key])
        # ABOVE
        elif (key[0] - 1, key[1]) in hms:
            result += int(hm[key])
        # DOWN
        elif (key[0] + 1, key[1]) in hms:
            result += int(hm[key])
        # UPPER LEFT
        elif (key[0] - 1, key[1] - 1) in hms:
            result += int(hm[key])
        # UPPER RIGHT
        elif (key[0] - 1, key[1] + 1) in hms:
            result += int(hm[key])
        # DOWN LEFT
        elif (key[0] + 1, key[1] - 1) in hms:
            result += int(hm[key])
        # DOWN RIGHT
        elif (key[0] + 1, key[1] + 1) in hms:
            result += int(hm[key])
    if len(hm[key]) > 1:
        # LEFT OR RIGHT
        if (key[0], key[1][0] - 1) in hms:
            result += int(hm[key])
        elif (key[0], key[1][-1] + 1) in hms:
            result += int(hm[key])
        # ABOVE
        elif (key[0] - 1, key[1][0]) in hms:
            result += int(hm[key])
        elif (key[0] - 1, key[1][-1]) in hms:
            result += int(hm[key])
        # DOWN
        elif (key[0] + 1, key[1][0]) in hms:
            result += int(hm[key])
        elif (key[0] + 1, key[1][-1]) in hms:
            result += int(hm[key])
        # UPPER LEFT
        elif (key[0] - 1, key[1][0] - 1) in hms:
            result += int(hm[key])
        # UPPER RIGHT
        elif (key[0] - 1, key[1][-1] + 1) in hms:
            result += int(hm[key])
        # DOWN LEFT
        elif (key[0] + 1, key[1][0] - 1) in hms:
            result += int(hm[key])
        # DOWN RIGHT
        elif (key[0] + 1, key[1][-1] + 1) in hms:
            result += int(hm[key])
    if len(hm[key]) == 3:
        # ABOVE
        if (key[0] - 1, key[1][1]) in hms:
            result += int(hm[key])
        # DOWN
        elif (key[0] + 1, key[1][1]) in hms:
            result += int(hm[key])
            

print(result)