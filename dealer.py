from random import shuffle

class Dealer():
	"""docstring for dealer"""

	hand = []

	def __init__(self, deck):
		self.deck = deck

	def shuffle_deck(self):
		shuffle(self.deck)

	def deal_card_face_up(self, hand):
		self.deck[0].facing_up = True
		hand.append(self.deck[0])
		self.deck.pop(0)

	def deal_card_face_down(self, hand):
		hand.append(self.deck[0])
		self.deck.pop(0)
		