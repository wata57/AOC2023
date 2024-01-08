win_num = []
play_num = []
winning = {}
player = {}
result = 0

with open('input.txt', 'r') as file:
    data = file.read()
    s = data.strip().split('\n')

for card in s:
    # SEPARATING CARD FROM CONTENT
    y = card.split(': ')[1]
    # SEPARATING WINNING NUMBERS FROM PLAYER NUMBERS
    winning_n, player_n = y.split(' | ')
    win_num.append(winning_n)
    play_num.append(player_n)
 
# CREATING A DICTIONARY: KEY = CARD NUMBER |||| VALUE = LIST OF WINNING NUMBERS ON THAT CARD
for i, sequence in enumerate(win_num):
    numbers = sequence.split(' ')
    winning[i+1] = numbers

# CREATING A DICTIONARY: KEY = CARD NUMBER |||| VALUE = LIST OF PLAYER NUMBERS ON THAT CARD
for i, sequence in enumerate(play_num):
    numbers = sequence.split(' ')
    player[i+1] = numbers

c = 0

for i in range(1,195):
    for number in player[i]:
        if number != '':
            if number in winning[i]:
                c += 1
    if c == 1:
        result += 1
    elif c > 1:
        result += 2**(c-1)
    print('\n')
    c = 0
    print(result)

