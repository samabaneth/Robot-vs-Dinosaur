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

        self.robot.attack(self.dinosaur)
        print('\nMichael smacked Cora with the scepter! Cora took 20 damage! Coras remaining health:\n')
        print(self.dinosaur.health)
        
        self.dinosaur.attack(self.robot) 
        print('\nCora chomped Michael! Michael took 25 damage! Michaels remaining health:\n')
        print(self.robot.health)
        
    def victory(self): 
        if self.robot.health <= 0:
            print('\nCongratulations Cora, you defeated Michael!\n')
