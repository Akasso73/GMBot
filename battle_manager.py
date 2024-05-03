import random

class Warrior:
    def __init__(self, name: str, health: int, strength: int, agility: int, magic: int):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.magic = magic

    def copy(self):
        return Warrior(self.name, self.health, self.strength, self.agility, self.magic)

class BattleManager:
    def __init__(self, character1: Warrior, character2: Warrior):
        self.character1 = character1
        self.character2 = character2

    def attack_physical(self, attacker: Warrior, target: Warrior):
        damage = attacker.strength * random.uniform(0.8, 1.2)
        target.health -= damage

    def attack_magical(self, attacker: Warrior, target: Warrior):
        damage = attacker.magic * random.uniform(0.8, 1.2)
        target.health -= damage

def start_battle(character1: Warrior, character2: Warrior):
    character1 = character1.copy()
    character2 = character2.copy()

    battle_manager = BattleManager(character1, character2)
    battle_manager.attack_magical(character1, character2)
    battle_manager.attack_physical(character2, character1)

    print(f"{character1.name} health: {character1.health}")
    print(f"{character2.name} health: {character2.health}")

a = Warrior("Warrior1", 100, 10, 10, 10)
b = Warrior("Warrior2", 100, 10, 10, 10)

start_battle(a, b)

print(f"{a.name} health: {a.health}")
print(f"{b.name} health: {b.health}")