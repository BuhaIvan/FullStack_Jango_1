class Character:
    # атрибуты уровня класса
    max_speed = 100
    dead_health = 0

    def __init__(self, race, damage=10, armor=20):
        # По сути race, damage и armor - это атрибуты объекта класса (то есть пользователь сможет ими пользоваться
        # только после того как создаст объект класса)
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == Character.dead_health

unit = Character("Ork")

print(Character.max_speed) # 100 (можно получить без создания объекта)
# print(Character.race) # AttributeError: type object 'Character' has no attribute 'race'

# нанесли урон
unit.hit(44)
# узнали сколько осталось жизней
print(unit.health) # 56
# узнали жив ли персонаж
print(unit.is_dead()) # False