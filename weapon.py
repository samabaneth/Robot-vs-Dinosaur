
class Weapon:
    def __init__ (self, name, attack_power):
        self.name = "scepter"
        self.attack_power = 25

    def hit_cora(self, cora_health):
        self.attack_power -= cora_health
        