from robot import Robot

class Dinosaur:
    def __init__(self):
        self.name = "Cora"
        self.health = 100
        self.attack_power = 25

    def attack(self, robot):
        robot.health -= self.attack_power
