class Player():

    bankroll = 500
    handValue = 0
    isBusted = False

    def __init__(self, username):
        self.hand = []
        self.username = username
        
    
    def viewHand(self):
        print("-----------------------------------")
        print(self.username)
        print("-----------------------------------")
        for card in self.hand:
            print(card)
            print("-----------------------------------")