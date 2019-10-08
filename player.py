class Player():

    def __init__(self, username):
        self.hand = []
        self.bankroll = 500
        self.username = username
    
    def viewHand(self):
        print("-----------------------------------")
        print(self.username)
        print("-----------------------------------")
        for card in self.hand:
            print(card)
            print("-----------------------------------")
