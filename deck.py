from card import Card
from random import shuffle

class Deck():

    def __init__(self):
        self.cards = self.__createDeck()

    def __createDeck(self):
        cards = []

        for x in range (1, 5):
            for y in range(1, 14):
                cards.append(Card(self.__setCardNumber(y), self.__setCardColor(x), self.__setCardSuit(x)))
        
        return cards

    def __setCardColor(self, number):
        if number % 2 == 0:
            return "Red"
        else:
            return "Black"

    def __setCardSuit(self, number):
        suits = ["Spades", "Hearts", "Clovers", "Diamonds"]

        return suits[number - 1]

    def __setCardNumber(self, number):
        special_cards = ["Ace", "Jack", "Queen", "King"]

        if number == 1:
            return special_cards[number - 1]
        elif number > 10:
            return special_cards[number - 10]
        else:
            return number
    
    def shuffleDeck(self):
        shuffle(self.cards)