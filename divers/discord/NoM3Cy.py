from pymox_kit import *

class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur", pseudo, "/Points de vie: ", health, "/ Attaque", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        damage = self.attack

class Warrior(Player):

    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("Bienvenue au guerrier", pseudo, "/Points de vie: ", health, "/ Attaque", attack)

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 1
        super().damage(damage)

    def attack_player(self, target_player):
        damage = self.attack

    def blade(self):
        self.armor = 3
        print("Les points d'arumres ont été recharger.")

    def get_armor_point(self):
        return self.armor


if __name__ == "__main__":
    
    cls()
    
    print(title_fr())
    print('\nok')
    
    player = Player("Graven", 20, 2)
    player.damage(3)
    warrior = Warrior("DarkWarrior", 30, 4)
    warrior.damage(4)
    print("vie:", warrior.get_health(), "armure:", warrior.get_armor_point())

    warrior.damage(4)
    print("vie:", warrior.get_health(), "armure:", warrior.get_armor_point())

    warrior.damage(4)
    print("vie:", warrior.get_health(), "armure:", warrior.get_armor_point())

    if issubclass(Warrior, Player):
        print("Le guerrier est bien une specialisation de Player")

    end()

