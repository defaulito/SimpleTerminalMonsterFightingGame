import os
import random
import json

class Monster:
    
    allMonsters = []
    def __init__(self, attack:int = 0, defense:int = 0, health:int = 1, scoreAmount:int = 0, drops:list = []):
        assert attack >= 0, 'attack cannot be negative'
        assert defense >= 0, 'defense cannot be negative'
        assert health > 0, 'health cannot be negative or 0'
        
        self.__name = self.__class__.__name__
        self.__data = {'atk': attack, 'def': defense, 'health': health, 'maxhealth': health, 'scoreAmount': scoreAmount, 'drops': drops}
        self.__drop = self.__data['drops'][random.randint(0, len(self.__data['drops']) -1 )]
        
        Monster.allMonsters.append(self)
    # Attribute Encapsulation and limitng:
    @property
    def name(self):
        return self.__name
    
    @property
    def atK(self):
        return self.__data['atk']
    @atK.setter
    def atK(self, value):
        self.__data['atk'] = value
        if self.__data['atk'] < 0: # Limitng atK to always be greater than or equal 0
            self.__data['atk'] = 0
    
    @property
    def deF(self):
        return self.__data['def']
    @deF.setter
    def deF(self, value):
        self.__data['def'] = value
        if self.__data['def'] < 0:
            self.__data['def'] = 0
    
    @property
    def health(self):
        return self.__data['health']
    @health.setter
    def health(self, value):
        self.__data['health'] = value
        if self.__data['health'] < 0:
            self.__data['health'] = 0
        if self.__data['health'] > self.maxHealth:
            self.__data['health'] = self.maxHealth
    
    @property
    def maxHealth(self):
        return self.__data['maxhealth']
    @maxHealth.setter
    def maxHealth(self, value):
        self.__data['maxhealth'] = value
        if self.__data['maxhealth'] < 1:
            self.__data['maxhealth'] = 1
    
    @property
    def scoreAmount(self):
        return self.__data['scoreAmount']
    
    @property
    def drop(self):
        return self.__drop
    
    @property
    def icon(self):
        icon = self.__icon + self.__return_data()
        return icon
    
    def attack(self, player):
        player.health = player.health - self.atK
        
    def defend(self):
        self.health = self.health + self.deF
        
    def __return_data(self):
        return f"[{self.name}][A:{self.atK} D:{self.deF} H:{self.health}]\n"
        
    def __repr__(self):
        return(f"{self.name}({self.atK}, {self.deF}, {self.health}")

class Player:
    def __init__(self, attack: int = 5, defense: int = 5, health: int = 100):
        assert attack >= 0, 'attack cannot be negative'
        assert defense >= 0, 'defense cannot be negative'
        assert health > 0, 'health cannot be negative or 0'
        
        self.score = 0
        self.initialATK = attack
        self.initalDEF = defense
        self.initalHealth = health
        self.data = {'atk': attack, 'def': defense, 'health': health, 'maxhealth': health, 'inventory': []}
    
    # Attribute Encapsulation and limiting:
    @property
    def atK(self):
        return self.data['atk']
    @atK.setter
    def atK(self, value):
        self.data['atk'] = value
        if self.data['atk'] < 0:
            self.data['atk'] = 0

    @property
    def deF(self):
        return self.data['def']
    @deF.setter
    def deF(self, value):
        self.data['def'] = value
        if self.data['def'] < 0:
            self.data['def'] = 0
    
    @property
    def health(self):
        return self.data['health']
    @health.setter
    def health(self, value):
        self.data['health'] = value
        if self.data['health'] < 0:
            self.data['health'] = 0
        if self.data['health'] > self.maxHealth:
            self.data['health'] = self.maxHealth
        
    @property
    def maxHealth(self):
        return self.data['maxhealth']
    @maxHealth.setter
    def maxHealth(self, value):
        self.data['maxhealth'] = value
        if self.data['maxhealth'] < 1:
            self.data['maxhealth'] = 1
    
    @property
    def inventory(self):
        return self.data['inventory']
    @inventory.setter
    def inventory(self, value):
        self.data['inventory'] = value
    
    def attack(self, enemy: Monster):
        enemy.health = enemy.health - self.atK
    
    def defend(self):
        self.health = self.health + self.deF
    
    def __repr__(self):
        return 'Player()'

class Item:
    def __init__(self, price:int = 0):
        self.__name = (self.__class__.__name__).replace('_', ' ')
        self.price = 0

    @property
    def name(self):
        return self.__name
    
    @property
    def character(self):
        return self.__character
    
    def __repr__(self):
        return f"({self.__character}){self.name}"
    
class Battle:
    log =''
    
    @staticmethod
    def __clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def __player_input(player: Player, enemy: Monster):
        x = input(f"what would you like to do?\n(A)ttack:{player.atK} | (D)efend:{player.deF} | (I)nventory | (N)othing\n> ")
        if x.upper() == 'A':
            player.attack(enemy)
            Battle.log = Battle.log + f"\n* you attacked {enemy.name} for {player.atK} points"
            return
        elif x.upper() == 'D':
            player.defend()
            Battle.log = Battle.log + f"\n* you healed by {player.deF} points"
            return
        elif x.upper() == 'N':
            Battle.log = Battle.log + f"\n* you did nothing"
            return
        elif x.upper() == 'I':
            print(f"inventory: {player.inventory}\n")
                
        for item in player.inventory:
            if x.upper() == item.character:
                item.use(player, enemy)
                Battle.log = Battle.log + f"\n* you used {item.name}"                    
                return
        else:
            Battle.__player_input(player, enemy)
    
    @staticmethod
    def __monster_decide(player: Player, enemy: Monster):
        y = random.randint(0, 1)
        if (y == 1 or enemy.health <= enemy.deF) and enemy.health < enemy.maxHealth:
            enemy.defend()
            Battle.log = Battle.log + f"\n* {enemy.name} healed by {enemy.deF} points"    
        else:
            enemy.attack(player)
            Battle.log = Battle.log + f"\n* {enemy.name} attacked you for {enemy.atK} points"        
    
    @staticmethod
    def __player_death(player):
        skull = ''' 
     .-----.
    /      \\\\\\
    | 0   0 |
    \   ^   / 
     | ||| | 
       ||| 
'''
        Battle.__clear_terminal()
        print(skull)
        print(f"* you fainted\n\nyour score was {player.score}")
        player.score = 0
        player.inventory = []

    @staticmethod
    def start(player: Player, enemy: Monster):
        Battle.__clear_terminal()
        print(f'\n* you approach a {enemy.name}!')
        # Battle gameplay loop
        while True:
            print(enemy.icon)
            Battle.__monster_decide(player, enemy)
            Battle.__player_input(player, enemy)
            Battle.__clear_terminal()
            Battle.log = Battle.log + f"\n* your health is now {player.health}"
            print(Battle.log)
            Battle.log = ''

            if enemy.health == 0:
                Battle.__clear_terminal()
                print(f"* you defeated {enemy.name}!")
                player.score += enemy.scoreAmount
                drop = enemy.drop
                player.inventory.append(drop)
                print(f"* {enemy.name} dropped {drop.name}, it has been added to your inventory\n\nyour score is {player.score}")
                #exit()
                return
            elif player.health == 0:
                Battle.__player_death(player)
                player.score = 0
                return
                