from mainclass import Monster
from mainclass import Item
from items import *

class Slimy(Monster):
    def __init__(self):
        super().__init__(
            attack=4, defense=6, health=100, scoreAmount=5,
            
            drops=[Poison_Of_Damage(), Potion_Of_Strength()]
        )
        
        self._Monster__icon ='''
       _.
     / 0 )  
    ( ..  \ '''

class Spiky(Monster):
    def __init__(self):
        super().__init__(
            attack=7, defense=3, health=100, scoreAmount=4,
            
            drops=[Potion_Of_Strength(), Poison_Of_Weakening()]
        )
        
        self._Monster__icon ='''
       ^
     / 0 >>
    < ..  \ '''

class Cupcake(Monster):
    def __init__(self):
        super().__init__(
            attack=3, defense=3, health=100, scoreAmount=3,
            
            drops=[Poison_Of_Damage(), Poison_Of_Weakening()]
        )
        
        self._Monster__icon ='''
     (  0  )
    (__..___)
     \_\_/_/  '''

class Donut(Monster):
    def __init__(self):
        super().__init__(
            attack=4, defense=3, health=100, scoreAmount=3,
            
            drops=[Poison_Of_Damage(), Poison_Of_Weakening()]
        )
        
        self._Monster__icon ='''
     /   \\\\
    | (0) ||
     \..__/  '''

class Grumpy(Monster):
    def __init__(self):
        super().__init__(
            attack=6, defense=4, health=100, scoreAmount=7,
            
            drops=[Potion_Of_Strength(), Poison_Of_Weakening()]
        )
        
        self._Monster__icon ='''
     ^_____^
    / 0. .0 \\
    ( -^-^- ) '''
    
class Yeti(Monster):
    def __init__(self):
        super().__init__(
            attack=8, defense=5, health=100, scoreAmount= 10,
            
            drops=[Potion_Of_Healing(), Poison_Of_Damage()]
        )

        self._Monster__icon ='''
       _____
    //(0. .0)\\\\
     ( -^-^- )  '''