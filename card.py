class Card():

    visible = False

    def __init__(self, number, color, suit):
        self.number = number
        self.color = color
        self.suit = suit

    def __str__(self):
        if not self.visible:
            return "Number: ???\nColor: ???\nSuit: ???\n"
        else:
            return f"Number: {self.number}\nColor: {self.color}\nSuit: {self.suit}\n"
