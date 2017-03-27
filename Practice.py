rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

def buildDeck(rank, suit):
    bd = [n + 'of' + m in rank for m in suit]

print bd