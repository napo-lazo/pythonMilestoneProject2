from player import Player
from deck import Deck

def dealFaceUp(player, deck):
    player.hand.append(deck.cards.pop())
    player.hand[-1].isVisible = True

def dealFaceDown(player, deck):
    player.hand.append(deck.cards.pop())

def placeBet(player):
    while True:
        try: 
            bet = int(input(f"How much do you want to bet? (Current bankroll: {player.bankroll})\n"))
        except:
            print("That is not a valid input")
        else:
            if player.bankroll - bet >= 0:
                player.bankroll -= bet
                return bet
            else:
                print("You don't have enough money for that bet")

def initialSetup(players, deck):
    pot = placeBet(players[0])
    for _ in range(0,100):
        deck.shuffleDeck()
    dealFaceUp(players[0], deck)
    dealFaceUp(players[1], deck)
    dealFaceUp(players[0], deck)
    dealFaceDown(players[1], deck)
    return pot

def getCardValue(card):
    if(not card.isVisible):
        return 0

    try:
        value = int(card.number)
    except:
        if card.number == "Ace":
            return 11
        elif card.number == "Jack" or "Queen" or "King":
            return 10
    else:
        return value

def checkHandValue(hand):
    totalValue = 0
    
    cardValues = list (map(getCardValue, hand))
    
    cardValues.sort()
    for value in cardValues:
        if value == 11 and totalValue + 11 > 21:
            totalValue += 1
        else:
            totalValue += value

    return totalValue

def viewTable(players):
    for player in players:
        print("------------------------------------------")
        print(player.username)
        for card in player.hand:
            print("------------------------------------------")
            print(card)

        player.handValue = checkHandValue(player.hand)
        print("------------------------------------------")
        if player.handValue > 21:
            print(f"Total value: {player.handValue} - BUSTED")
            player.isBusted = True
        else:
            print(f"Total value: {player.handValue}")
        print("------------------------------------------") 

def round(players, deck, pot):

    isTurnOver = False

    while not isTurnOver:
        viewTable(players)
        if players[0].handValue < 21: 
            isTurnOver = playerTurn(players[0], deck)
        else:
           isTurnOver = True 

    if players[0].handValue < 21 and not players[0].isBusted:
        cpuwins = cpuTurn(players[0], players[1], deck)
    elif players[0].handValue == 21:
        cpuwins = False
    else:
        cpuwins = True

    viewTable(players)
    if not cpuwins:
        print("------------------------------------------")
        print(f"PLAYER WINS, you get {pot * 2}")
        print("------------------------------------------")
        players[0].bankroll += pot * 2
    else:
        print("------------------------------------------")
        print("CPU WINS")
        print("------------------------------------------")

def playerTurn(player, deck):
        while True:
            answer = input("Hit or leave?\n")
            if answer.lower() == "hit" or answer.lower() == "h":
                dealFaceUp(player, deck)
                return False
            elif answer.lower() == "leave" or answer.lower() == "l":
                return True

def cpuTurn(player, cpu, deck):
    cpu.hand[-1].isVisible = True

    while True:
        cpu.handValue = checkHandValue(cpu.hand)
        if cpu.handValue > 21:
            return False
        elif cpu.handValue > player.handValue:
            return True
        else:
            dealFaceUp(cpu, deck)



def endOfRound(players, deck):
    for player in players:
        size = len(player.hand)
        for _ in range(0, size):
            player.hand[-1].isVisible = False
            deck.cards.append(player.hand.pop())
        player.isBusted = False
        player.handValue = 0
    deck.shuffleDeck()

def blackjackMain():
    players = [Player("Player"), Player("Cpu")]
    deck = Deck()
    continuePlaying = True

    while players[0].bankroll > 0 and continuePlaying:
        pot = initialSetup(players, deck)
        round(players, deck, pot)
        endOfRound(players, deck)

        if(players[0].bankroll > 0):
            while True:
                answer = input("Do you want to play another round?\n")
                if answer.lower() == "no" or answer == "n":
                    continuePlaying = False
                    break
                elif answer.lower() == "yes" or answer == "y":
                    break
        else:
            print("You ran out of chips")
            print("------------------------------------------")


if __name__ == "__main__":
    blackjackMain()