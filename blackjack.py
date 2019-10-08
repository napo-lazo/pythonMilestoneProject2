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
    dealFaceDown(players[1], deck)
    dealFaceUp(players[0], deck)
    dealFaceUp(players[1], deck)
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
    cardValues = []
    totalValue = 0
    
    for card in hand:
        cardValues.append(getCardValue(card))
    
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
        print("------------------------------------------")
        print(f"Total value: {checkHandValue(player.hand)}")
        print("------------------------------------------")

if __name__ == "__main__":
    players = [Player("Player"), Player("Cpu")]
    deck = Deck()

    pot = initialSetup(players, deck)
    viewTable(players)
    while False:
        pass
