import colorama 


class Player():
	"""docstring for Player"""

	hand = []
	chips = 500

	def bet(self, quantity):
		while True:
			if(self.chips - quantity > 0):
				self.chips = self.chips - quantity
				bet = quantity
				return bet
			else:
				print(colorama.Fore.RED, "You don't have enough chips")
				print(colorama.Style.RESET_ALL)
				return