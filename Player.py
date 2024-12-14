import random

class Player:

    def __init__(self, n = "Гейрой"):
        self.intelligent = random.randint(5,15)
        self.strength = random.randint(5,15)
        self.charisma = random.randint(5,15)
        self.type = 1
        self.name = n

    def reset_char(self):
        Player.intelligent = random.randint(5, 15)
        Player.strength = random.randint(5, 15)
        Player.charisma = random.randint(5, 15)