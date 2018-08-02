import colorama 
colorama.init()


class Player():
	"""docstring for Player"""

	hand = []
	chips = 500

	def set_bet(self):

		while True:
			try:
				print(colorama.Fore.GREEN, f"Current amount of chips: {self.chips}")
				print(colorama.Style.RESET_ALL)
				quantity = int(input("How much do you want to bet?\n"))
			except:
				print(colorama.Fore.RED, "That is not a number, please enter a number")
				print(colorama.Style.RESET_ALL)
			else:
				bet = self.check_chips_availability(quantity)
				if(bet):
					break
				else:
					print(colorama.Fore.RED, "You can't bet 0 chips")
					print(colorama.Style.RESET_ALL)
		return quantity

	def check_chips_availability(self, quantity):
		while True:
			if(self.chips - quantity > 0):
				self.chips = self.chips - quantity
				bet = quantity
				return bet
			else:
				print(colorama.Fore.RED, "You don't have enough chips")
				print(colorama.Style.RESET_ALL)
				return