from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = "Michael"
        self.health = 100
        self.weapon = Weapon("scepter", 20)
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power