from random import shuffle

class Dealer():
	"""docstring for dealer"""

	hand = []

	def __init__(self, deck):
		self.deck = deck

	def shuffle_deck(self):
		shuffle(self.deck)

	def deal_card(self, hand):
		hand.append(self.deck[0])
		self.deck.pop(0)
		