from statistics import correlation
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.robot = Robot()
    def welcome(self):
        print('\nShall we play a game?\n')
    def fight(self):
       while self.dinosaur.health > 0 and self.robot.health > 0:
        self.dinosaur.attack(self.robot) 
        print(self.robot.health)
        print('\nCora chomped Michael!\n')
    def victory(self):
        if self.dinosaur.health < 0:
            print('\nCongratulations Michael\n')
        if self.robot.health < 0:
            print('\nCongratulations Cora\n')
