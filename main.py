import os
import random
import json
from mainclass import *
from monsters import *
from items import *

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_screen():
    clear_terminal()
    x = input("welcome!\n(S)tart | (Q)uit\n> ")
    if x.upper() == 'S':
        return
    elif x.upper() == 'Q':
        exit()
    else:
        start_screen()

def play_again():
    x = input("\nplay again?\n(Y)es | (N)o\n> ")
    if x.upper() == 'Y':
        clear_terminal()
        return
    elif x.upper() == 'N':
        quit()
    else:
        play_again()

def save(player: Player):
    inventory = []
    for item in player.inventory:
        inventory.append(item.name)
    
    with open('playerinfo.json', 'a') as f:
        f.truncate(0)
        playerinfo = {
            "inventory": inventory,
            "score": player.score
        }
        json.dump(playerinfo, f, indent=4)

def load(player: Player):
    with open('./playerinfo.json', 'r') as f:
        data = json.load(f)
        for item in data['inventory']:
            if item == 'Poison Of Weakening':
                player.inventory.append(Poison_Of_Weakening())
            if item == 'Poison Of Damage':
                player.inventory.append(Poison_Of_Damage())
            if item == 'Potion Of Strength':
                player.inventory.append(Potion_Of_Strength())
            if item == 'Potion Of Healing':
                player.inventory.append(Potion_Of_Healing())
                
        player.score = data['score']

def main():
    start_screen()
    player = Player()
    load(player)
 
    for monster in Monster.allMonsters:
        monsters.append(monster)
    # main loop
    while True:
        monsters = [Slimy(), Spiky(), Cupcake(), Donut(), Grumpy(), Yeti()]
        monster0 = monsters[random.randint(0, len(monsters)-1)]
        player.atK = player.initialATK
        player.deF = player.initalDEF
        player.health = player.initalHealth
        Battle.start(player, monster0)
        save(player)
        play_again()

main()