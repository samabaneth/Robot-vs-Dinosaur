from robot import Robot

class Dinosaur:
    def __init__(self, cora):
        self.name = "Cora"
        self.health = 100
        self.attack_power = 25
        self.attack = "chomp"
        self.cora = cora

    def attack(self, michael):
        self.attack_power -= michael
