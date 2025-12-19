from abc import ABC, abstractmethod


class atackManager(ABC):
    @abstractmethod
    def attack(self, superhero):
        pass


# Implementaciones concretas
class PunchAttack(atackManager):
    def attack(self, superhero):
        return f"{superhero.name} attacks with a powerfull punch!!!! "


class LaserAttack(atackManager):
    def attack(self, superhero):
        return f"{superhero.name} attacks with a long laser!!!"


class FireballAttack(atackManager):
    def attack(self, superhero):
        return f"{superhero.name} attacks with a big fire ball!!!"


class IceballAttack(atackManager):
    def attack(self, superhero):
        return f"{superhero.name} attacks with a big ice ball!!!"


class Superhero:
    def __init__(self, name, health, atackManager) -> None:
        self.name = name
        self.health = health
        self.atackManager = atackManager

    def attack(self):
        return self.atackManager.attack(self)


class Game:
    def __init__(self) -> None:
        self.superheroes = []

    def add_superheroes(self, superhero):
        self.superheroes.append(superhero)

    def superheroe_action(self):
        for superhero in self.superheroes:
            print(superhero.attack())


game = Game()
superman = Superhero("Superman", 100, PunchAttack())
cyclops = Superhero("Cyclops", 80, LaserAttack())
fireman = Superhero("Fireman", 120, PunchAttack())
iceman = Superhero("Iceman", 120, IceballAttack())

game.add_superheroes(superman)
game.add_superheroes(cyclops)
game.add_superheroes(fireman)
game.add_superheroes(iceman)

game.superheroe_action()
