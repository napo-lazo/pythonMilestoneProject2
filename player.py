class Player():
	"""docstring for Player"""

	hand = []
	chips = 500

	def bet(self, quantity):
		if(self.chips - quantity > 0):
			return bet
		else:
			print("You don't have enough chips")
		