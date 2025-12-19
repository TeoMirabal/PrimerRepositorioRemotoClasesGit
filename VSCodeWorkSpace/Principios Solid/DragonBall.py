from abc import ABC, abstractmethod

class AttackManager(ABC):
    @abstractmethod
    def attack(self, Superhero):
        pass

class KamehamehaAttack(AttackManager):
    def attack(self, Superhero):
        return f"{Superhero.name} lanza un poderoso Kame...hame...HAAAAA"
    
class ResplandorFinalAttack(AttackManager):
    def attack(self, Superhero):
        return f"{Superhero.name} lanza un poderoso Resplandor...FINAAAAAL"
    
class Superhero:
    def __init__(self, name, attack_type):
        self.name = name
        self.attack_type = attack_type
    


Goku = Superhero("Goku", KamehamehaAttack)

Vegueta = Superhero("Vegueta", ResplandorFinalAttack)
