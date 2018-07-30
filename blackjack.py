from card import create_deck
from dealer import Dealer
from player import Player

if __name__ == '__main__':
	dealer = Dealer(create_deck())
	player = Player()
	playing = True

	