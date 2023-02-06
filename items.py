import math
from mainclass import *

class Poison_Of_Weakening(Item):
    def __init__(self):
        super().__init__(
            price=0
        )

        self._Item__character ='0'
        
    def use(self, player: Player, enemy: Monster):
        enemy.atK = math.floor(enemy.atK * (2/3))
        enemy.deF = math.floor(enemy.deF * (3/4))
        
        player.inventory.remove(self)

class Poison_Of_Damage(Item):
    def __init__(self):
        super().__init__(
            price=0
        )
        
        self._Item__character = '1'
    
    def use(self, player: Player, enemy: Monster):
        enemy.health = math.floor(enemy.health * (3/4))
        
        player.inventory.remove(self)
        
class Potion_Of_Strength(Item):
    def __init__(self):
        super().__init__(
            price=0
        )

        self._Item__character = '2'
        
    def use(self, player: Player, enemy: Monster):
        player.atK = player.atK + 2
        
        player.inventory.remove(self)
        
class Potion_Of_Healing(Item):
    def __init__(self):
        super().__init__(
            price=0
        )
        
        self._Item__character = '3'
        
    def use(self, player: Player, enemy: Monster):
        player.health = player.maxHealth
        
        player.inventory.remove(self)