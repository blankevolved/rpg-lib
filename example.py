from rpg import Player, Item, Enemy, Weapons, Armor


player = Player(health=10, damage=1, regen=.1)

sword = Weapons.Weapon('Sword')

player.equip(sword)

print(player.equipped)

print(player.damage)

enemy = Enemy('goblin', health=5, damage=1, regen=.1)

player.fight(enemy)

