import os

class Meta:
    def clear():
 
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = os.system('clear')


class Entity:
    def __init__(self, health: int, damage: int, regen: int):
        self.health     = health
        self.max_health = health
        self.damage     = damage
        self.regen      = regen

class Item:
    def __init__(self, name: str, slot: str, boost_type: str, boost_num: int):
        self.name       = name
        self.boost_type = boost_type
        self.boost_num  = boost_num
        self.slot       = slot

class Weapons:
    class Weapon(Item):
        def __init__(self, name: str, slot='main_hand', boost_type='damage', boost_num=1):
            super().__init__(name, slot, boost_type, boost_num)

    class Shield(Item):
        def __init__(self, name: str, slot='off_hand', boost_type='health', boost_num=1):
            super().__init__(name, slot, boost_type, boost_num)

class Armor:
    class Helmet(Item):
        def __init__(self, name: str, slot='head', boost_type='health', boost_num=1):
            super().__init__(name, slot, boost_type, boost_num)

    class Chestplate(Item):
        def __init__(self, name: str, slot='chest', boost_type='health', boost_num=1):
            super().__init__(name, slot, boost_type, boost_num)

    class Leggings(Item):
        def __init__(self, name: str, slot='legs', boost_type='health', boost_num=1):
            super().__init__(name, slot, boost_type, boost_num)

    class Boots(Item):
        def __init__(self, name: str, slot='feet', boost_type='health', boost_num=1):
            super().__init__(name, slot, boost_type, boost_num)

class Enemy(Entity):
    def __init__(self, name: str, health: int, damage: int, regen: int):
        super().__init__(health, damage, regen)
        self.name = name
    
    def stats(self, space_at_start=False, space_at_end=False):
        if space_at_start == True:
            print()
        print(f'{self.name}:')
        print(f'\tHP: {self.health}/{self.max_health}')
        print(f'\tDMG: {self.damage}')
        print(f'\tREGEN: {self.regen}')
        if space_at_end == True:
            print()

class Player(Entity):
    def __init__(self, health: int, damage: int, regen: int, coins: int):
        super().__init__(health, damage, regen)
        self.inv = {}
        self.equipped = {
            'main_hand':{},
            'off_hand':{},
            'head':{},
            'chest':{},
            'legs':{},
            'feet':{}
        }
        self.coins = coins
    
    def stats(self, space_at_start=False, space_at_end=False):
        if space_at_start == True:
            print()
        print(f'HP: {self.health}/{self.max_health}')
        print(f'DMG: {self.damage}')
        print(f'REGEN: {self.regen}')
        if space_at_end == True:
            print()

    def equip(self, item: Item):
        if item.slot in self.equipped:
            if item.boost_type == 'health':
                self.max_health = self.max_health + item.boost_num
            elif item.boost_type == 'damage':
                self.damage = self.damage + item.boost_num
            
            self.equipped[item.slot] = {
                'name':item.name,
                'boost_type':item.boost_type,
                'boost_num':item.boost_num
            }
    def check_death(self):
        if self.health <= 0:
            self.coins = self.coins / 2
            return True
        else:
            return False
    
    def kill(self):
        self.health = 0
        self.check_death()
    def fight(self, enemy: Enemy):
        while True:
            self.stats(space_at_end=True)
            enemy.stats(space_at_end=True)
            print('1. Attack')
            
            inp = input('>>> ')

            if inp == '1':
                self.health = self.health - enemy.damage
                enemy.health = enemy.health - self.damage

            if enemy.health <= 0:
                break
            if self.check_death() == True:
                break
            
            Meta.clear()
