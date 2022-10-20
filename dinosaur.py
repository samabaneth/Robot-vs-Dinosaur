
class Dinosaur:
    def __init__(self):
        self.name = "Cora"
        self.health = 100
        self.attack_power = 25
        self.attack = "chomp"
    def chomp_michael(self, michael_health):
        self.attack_power -= michael_health
