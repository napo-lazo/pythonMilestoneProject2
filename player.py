from chip import Chip

class Player():

    def __init__(self):
        self.hand = []
        self.bankroll = self.__getInitialChips()

    def __getInitialChips(self):
        bankroll = []
        
        for _ in range(0,3):
            bankroll.append(Chip("Black"))
        for _ in range(0,4):
            bankroll.append(Chip("Green"))
        for _ in range(0, 4):
            bankroll.append(Chip("Blue"))
        for _ in range(0, 8):
            bankroll.append(Chip("Red"))
        for _ in range(0, 10):
            bankroll.append(Chip("White"))
        return bankroll