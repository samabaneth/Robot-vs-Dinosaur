from robot import Robot
from dinosaur import Dinosaur

class Weapon:
    def __init__ (self, michael_weapon_passed, cora_weapon_passed):
        self.cora_weapon = cora_weapon_passed
        self.michael_weapon = michael_weapon_passed
    def cora_hits_michael(self, michael_health):
        self.michael_health -= michael_health
    def michael_hits_cora(self, cora_health):
        self.cora_health -= cora_health