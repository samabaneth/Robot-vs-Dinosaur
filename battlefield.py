from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.player_one = Dinosaur(100)
        self.player_two = Robot(100)
    def fight(self):
