from random import shuffle

class Card():
	"""docstring for Card"""
	def __init__(self, color, suit, text, number, value):
		self.color = color
		self.suit = suit
		self.text = text
		self.number = number
		self.value = value

	def __str__(self):
		return f"Color: {self.color}\nSuit: {self.suit}\nText: {self.text}\nNumber: {self.number}\nValue: {self.value}"

def create_suit_of_cards(color, suit, deck):
	specialchars = ["A", "J", "Q", "K"]

	for x in range(1,14):
		if(x == 1):
			deck.append(Card(color, suit, specialchars[0], x, [1,11]))
			specialchars.pop(0)
		elif(x > 10):
			deck.append(Card(color, suit, specialchars[0], x, 10))
			specialchars.pop(0)
		else:
			deck.append(Card(color, suit, str(x), x, x))

def create_deck():
	deck = []

	create_suit_of_cards("Red", "Diamonds", deck)
	create_suit_of_cards("Black", "Clubs", deck)
	create_suit_of_cards("Red", "Hearts", deck)
	create_suit_of_cards("Black", "Spades", deck)

	return deck

deck = create_deck()

shuffle(deck)

print(deck[51])
