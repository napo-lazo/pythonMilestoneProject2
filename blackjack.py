from card import create_deck
from dealer import Dealer
from player import Player
import colorama
colorama.init()

def call_bets(player):

	while True:
		try:
			print(colorama.Fore.GREEN, f"Current amount of chips: {player.chips}")
			print(colorama.Style.RESET_ALL)
			quantity = int(input("How much do you want to bet?\n"))
		except:
			print(colorama.Fore.RED, "That is not a number, please enter a number")
			print(colorama.Style.RESET_ALL)
		else:
			bet = player.bet(quantity)
			if(bet):
				break
	return bet

if __name__ == '__main__':
	dealer = Dealer(create_deck())
	player = Player()
	playing = True
	pot = 0

	while playing:
		dealer.shuffle_deck()
		pot += call_bets(player)
		print(f"Current pot: {pot}")
		break