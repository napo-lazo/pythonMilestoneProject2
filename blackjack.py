from card import create_deck
from dealer import Dealer
from player import Player
import colorama
colorama.init()

def player_turn(dealer, player):

	while True:
		answer = ""
		dealer.deal_card_face_up(player.hand)

		while answer != "hit" and answer != "stay":
			answer = input("Do want to hit or stay?\n")
			if(answer != "hit" and answer != "stay"):
				print(colorama.Fore.RED, "That is not a valid answer")
				print(colorama.Style.RESET_ALL)
		if (answer.lower() == "stay"):
			break
		elif(answer.lower() == "hit"):
			continue



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

		player_turn(dealer, player)

		break