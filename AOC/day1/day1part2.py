dict1 = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

set1 = set()
for key in dict1:
    set1.add(key)

with open('input.txt', 'r') as file:
    res = 0
    for line in file:
        i = 0
        j = len(line) - 1

        while True:
            if line[i].isdigit() and line[j].isdigit():
                    li = 0
                    hi = 5
                    x = line[i]
                    while li < i:
                        for key in set1:
                            if key in line[0:i]:
                                if key in line[li:hi]:
                                    x = dict1[key]
                                    break
                        if x == dict1[key]:
                            break
                        li += 1
                        hi += 1
                            

                    hj = len(line)
                    lj = hj - 5

                    y = line[j]
                    while hj > j:
                        for key in set1:
                            if key in line[j:len(line) + 1]:
                                if key in line[lj:hj]:
                                    y = dict1[key]
                                    break
                        if y == dict1[key]:
                            break
                        hj -= 1
                        lj -= 1

                    break


            elif line[i].isdigit() == False:
                i += 1
            elif line[j].isdigit() == False:
                j -= 1 
    

        res += int(str(x) + str(y))
    print(res)
