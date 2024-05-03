import random
import character_manager as cm
    
def attack(attacker: cm.Warrior, target: cm.Warrior,type: str):
    if type == "magical":
        damage = attacker.magic * random.randint(1,6)
    elif type == "physical":
        damage = attacker.strength * random.randint(1,6)
    target.health -= damage
    if target.health < 0:
        target.health = 0
    print(f"{attacker.name} zadał {damage} obrażeń {target.name}!\n{target.name} ma teraz {target.health} punktów życia\n")

def start_battle(character1: cm.Warrior, character2: cm.Warrior):
    character1 = character1.copy()
    character2 = character2.copy()
    isBattle = True
    if character1.agility > character2.agility:
        attacker = character1
        target = character2
    else:
        attacker = character2
        target = character1
    print(f"{attacker.name} zaczyna!\n")
    while isBattle:
        option = int(input("1. Atak fizyczny\n2. Atak magiczny\n"))
        if option == 1:
            attack(attacker, target, "physical")
        elif option == 2:
            attack(attacker, target, "magical")
        if target.health <= 0:
            print(f"{target.name} przegrał!")
            isBattle = False
            return
        print(f"{attacker.name} atakuje {target.name}\n")
        attacker, target = target, attacker
