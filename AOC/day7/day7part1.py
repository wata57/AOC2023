def is_five(mapcards, card):
    if max(mapcards.values()) == 5:
        fivek.append(card)

def is_four(mapcards, card):
    if max(mapcards.values()) == 4:
        fourk.append(card)

def is_fullhouse(mapcards, card):
    if 3 in mapcards.values() and 2 in mapcards.values():
        fullh.append(card)

def is_three(mapcards, card):
    if 3 in mapcards.values() and 2 not in mapcards.values():
        threek.append(card)

def is_twopair(mapcards, card):
    if list(mapcards.values()).count(2) == 2:
        twopair.append(card)

def is_onepair(mapcards, card):
    if max(mapcards.values()) == 2 and list(mapcards.values()).count(2) == 1:
        onepair.append(card)

def is_highcard(mapcards, card):
    if max(mapcards.values()) == 1:
        highcard.append(card)

def rank(hands):
    return sorted(hands, key=lambda item: [card_str[char] for char in item])

card_str = {
    'A': 14, 
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9, 
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4, 
    '3': 3,
    '2': 2,
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
    for char in card:
        if char not in mapcards:
            mapcards[char] = 1
        else:
            mapcards[char] += 1
    is_five(mapcards, card)
    is_four(mapcards, card)
    is_fullhouse(mapcards, card)
    is_three(mapcards, card)
    is_twopair(mapcards, card)
    is_onepair(mapcards, card)
    is_highcard(mapcards, card)

ranked_hands = rank(highcard) + rank(onepair) + rank(twopair) + rank(threek) + rank(fullh) + rank(fourk)+ rank(fivek)

result = 0

for i, hand in enumerate(ranked_hands):
    result += (i + 1) * int(cards_bids[hand])

print(result)


