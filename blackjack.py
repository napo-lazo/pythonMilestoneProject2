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

		dealer.deal_card_face_up(player.hand)
		dealer.deal_card_face_up(dealer.hand)
		dealer.deal_card_face_up(player.hand)
		dealer.deal_card_face_down(dealer.hand)

		# TO DO:
		# player's turn
		# dealer's turn
		# check winner

		break