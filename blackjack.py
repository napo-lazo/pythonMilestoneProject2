from card import create_deck
from dealer import Dealer
from player import Player	

if __name__ == '__main__':
	dealer = Dealer(create_deck())
	player = Player()
	playing = True
	pot = 0

	while playing:
		dealer.shuffle_deck()
		pot += player.set_bet()
		print(f"Current pot: {pot}")
		break