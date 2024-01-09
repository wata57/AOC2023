def is_five(mapcards, noJ, card):
    if max(mapcards.values()) == 5:
        fivek.append(card)
        return True
    elif max(noJ.values()) + mapcards.get('J', -1) == 5:
        fivek.append(card)
        return True
    return False

def is_four(mapcards, noJ, card):
    if max(mapcards.values()) == 4:
        fourk.append(card)
        return True
    elif max(noJ.values()) + mapcards.get('J', -1) == 4:
        fourk.append(card)
        return True
    return False

def is_fullhouse(mapcards, noJ, card):
    if 3 in mapcards.values() and 2 in mapcards.values():
        fullh.append(card)
        return True
    elif list(noJ.values()).count(2) == 2:
        if mapcards.get('J', -1) == 1:
            fullh.append(card)
            return True
    return False

def is_three(mapcards, noJ, card):
    if 3 in mapcards.values() and 2 not in mapcards.values():
        threek.append(card)
        return True
    if max(mapcards.values()) == 2 and list(mapcards.values()).count(2) == 1:
        if mapcards.get('J', -1) == 1:
            threek.append(card)
            return True
    if max(noJ.values()) == 1:
        if mapcards.get('J', -1) == 2:
            threek.append(card)
            return True
    return False

def is_twopair(mapcards, noJ, card):
    if list(mapcards.values()).count(2) == 2:
        twopair.append(card)
        return True
    return False

def is_onepair(mapcards, noJ, card):
    if max(mapcards.values()) == 2 and list(mapcards.values()).count(2) == 1:
        onepair.append(card)
        return True
    elif max(mapcards.values()) == 1:
        if mapcards.get('J', -1) == 1:
            onepair.append(card)
            return True
    return False

def is_highcard(mapcards, noJ, card):
    if max(mapcards.values()) == 1:
        highcard.append(card)
        return True
    return False

def rank(hands):
    return sorted(hands, key=lambda item: [card_str[char] for char in item])


card_str = {
    'A': 14, 
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9, 
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4, 
    '3': 3,
    '2': 2,
    'J': 1
}

with open('input.txt', 'r') as file:
    data = (file.read()).strip().split('\n')

cards_bids = {}
fivek = []
fourk = []
fullh = []
threek = []
twopair = []
onepair = []
highcard = []

for line in data:
    x, y = line.split(' ')
    cards_bids[x] = y

for card in cards_bids:
    mapcards = {}
    noJ = {}
    for char in card:
        if char not in mapcards:
            mapcards[char] = 1
            if char != 'J':
                noJ[char] = 1
        else:
            mapcards[char] += 1
            if char != 'J':
                noJ[char] += 1  
    if is_five(mapcards, noJ, card):
        continue
    if is_four(mapcards, noJ, card):
        continue
    if is_fullhouse(mapcards, noJ, card):
        continue
    if is_three(mapcards, noJ, card):
        continue
    if is_twopair(mapcards, noJ, card):
        continue
    if is_onepair(mapcards, noJ, card):
        continue
    if is_highcard(mapcards, noJ, card):
        continue


ranked_hands = rank(highcard) + rank(onepair) + rank(twopair) + rank(threek) + rank(fullh) + rank(fourk) + rank(fivek)

result = 0
c = 0
for i, hand in enumerate(ranked_hands):
    result += (i + 1) * int(cards_bids[hand])

print(result)