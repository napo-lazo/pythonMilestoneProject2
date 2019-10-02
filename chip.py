class Chip():

    def __init__(self, color):
        self.color = color
        self.value = self.__getChipValue

    def __getChipValue(self, color):
        if color == "White":
            return 1
        elif color == "Red":
            return 5
        elif color == "Blue":
            return 10
        elif color == "Green":
            return 25
        elif color == "Black":
            return 100
        