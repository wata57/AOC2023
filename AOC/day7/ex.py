def is_onepair(mapcards, noJ, card):
    if max(mapcards.values()) == 2 and list(mapcards.values()).count(2) == 1:
        onepair.append(card)
        return True
    elif max(mapcards.values()) == 1:
        if mapcards.get('J', -1) == 1:
            onepair.append(card)
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

with open('test.txt', 'r') as file:
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

