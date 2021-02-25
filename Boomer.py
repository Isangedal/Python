import os, random, math, time

class Boomer():
    name = None
    lvl = None
    hp = None
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    # Getters
    def get_name(self):
        return self.name
    def get_lvl(self):
        return self.lvl
    def get_hp(self):
        return self.hp
    # Setters
    def set_name(self, name):
        self.name = name
    def set_lvl(self, lvl):
        self.lvl = lvl
    def set_hp(self, hp):
        self.hp = hp

encounters = {"names": ["Sondre", "Bjørg", "Borg", "Mega Borg", "CyBorg"], "levels": [1, 5, 10, 25, 50], "hp": [5, 10, 25, 50, 100]}

hp = 10
max_hp = hp
attack_power = 1
defence = 1
xp = 0
req_exp = 5
lvl = 1

items = {"names": ["Apple", "Pear"], "desc": ["An apple a day keeps the boomer away", "A pear a day keeps the zoomer away"], "quantity": [1, 2], "heal": [5, 1]}

def clear(): os.system('cls')

def create_encounter(num):
    return Boomer(encounters.get("names")[num], encounters.get("levels")[num], encounters.get("hp")[num])

def start(encounter, num):
    clear()
    if hp <= 0:
        input("You died!\n")
        exit()
    else:
        if encounter.get_hp() <= 0:
            input(f"{encounter.get_name()} has been defeated!\n")
            start(create_encounter(num + 1), num + 1)
        print(f"{encounter.get_name()}: Level {encounter.get_lvl()}, HP: {encounter.get_hp()}\n")
        action = input("(A)ttack | (I)tem | (E)xit\n")
        if action.lower() == "a":
            attack(encounter, num)
        elif action.lower() == "i":
            item(encounter, num)
        elif action.lower() == "e":
            exit()
        else:
            start(encounter, num)

def attack(encounter, num):
    global hp, xp, attack_power, lvl

    clear()
    p_attack = attack_power
    encounter.set_hp(encounter.get_hp() - p_attack)
    encounter_attack = random.randint(1, math.ceil(encounter.get_lvl() / 2))
    xp_gained = random.randint(1, math.ceil(encounter.get_lvl() / 2))
    xp += xp_gained
    if xp >= req_exp:
        lvl += 1
        attack_power *= math.ceil(1.5)
        print(f"You leveled up to level {lvl}")
    hp -= encounter_attack
    for _ in range(3):
        os.system('color 40')
        time.sleep(0.01)
        os.system('color 07')
        time.sleep(0.01)
    input(f"You attacked {encounter.get_name()} and dealt {p_attack}.\n{encounter.get_name()} attacked you and dealt {encounter_attack} damage! You have {hp} hp left.\nYou got {xp_gained} exp.\n")
   
    start(encounter, num)

def item(encounter, num):
    global hp

    max_hp = hp+1
    clear()
    if hp == max_hp:
        clear()
        input("You already have full health.\n")
        start(encounter, num)
        return
    if len(items.get("names")) > 0:
        print("You have:\n")
        for i in range(len(items.get("names"))):
            print(f"{i+1}: {items.get('names')[i]} x{items.get('quantity')[i]}: {items.get('desc')[i]} - {items.get('heal')[i]}")
        item_use = input("\nWhich item would you like to use? (Type \"return\" to return)\n")
        if item_use.lower() != "return":
            try:
                clear()
                hp += items.get('heal')[int(item_use) - 1]
                if hp > max_hp: hp = max_hp
                input(f"You used a {items.get('names')[int(item_use) - 1]}")
                if items.get('quantity')[int(item_use) - 1] == 1:
                    del items.get('names')[int(item_use) - 1]
                else:
                    items.get('quantity')[int(item_use) - 1] -= 1
                start(encounter, num)
            except:
                clear()
                input("An error was found.")
                item(encounter)
        else: start(encounter, num)
    else:
        input("You do not have any items\n")
        start(encounter, num)

input("You have encountered a boomer!\n")
start(create_encounter(0), 0)