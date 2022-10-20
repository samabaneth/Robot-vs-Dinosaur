
class Weapon:
    def __init__ (self, name, attack_power):
        self.name = "scepter"
        self.attack_power = 25

    def attack(self, cora):
        self.attack_power -= cora
        