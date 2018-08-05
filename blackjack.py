from card import create_deck
from dealer import Dealer
from player import Player
import colorama
colorama.init()

def player_turn(dealer, player):

	while True:
		answer = ""

		player.print_hand()

		if(check_if_busted(player.hand)):
				print(colorama.Fore.RED, "BUSTED")
				print(colorama.Style.RESET_ALL)
				break

		while answer != "hit" and answer != "stay":
			answer = input("Do want to hit or stay?\n")
			if(answer != "hit" and answer != "stay"):
				print(colorama.Fore.RED, "That is not a valid answer")
				print(colorama.Style.RESET_ALL)
		if (answer.lower() == "stay"):
			break
		elif(answer.lower() == "hit"):
			dealer.deal_card_face_up(player.hand)
			continue


def check_if_busted(hand):
	total = 0
	aces_list = []

	for card in hand:
		if(card.text == "A"):
			aces_list.append(card)
		else:
			total += card.value

	for ace in aces_list:
		if(total + ace.value[1] or (total + ace.value[1] >= 21 and len(aces_list) > 1)):
			total += ace.value[0]
		else:
			total += ace.value[1]

	print(f"Hand value: {total}")
	return total > 21


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