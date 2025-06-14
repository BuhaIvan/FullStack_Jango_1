# Классы нужны, что бы описывать объекты (по сути это абстрактный объект)
# Класс - общее описание, который описывает общую сущность
# Объект - это экземпляр класса

# Создадим свой класс "герой"
class Character:
    # Конструктор класса
    # self - ссылка на экземпляр. Через self мы имеем доступ к экземпляру класса изнутри самого класса
    # вторая переменная - присваивается атрибуту на уровне метода класса (их может быть больше)
    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor

# Экземпляр класса
unit = Character("Human", 40, 33)
print(type(unit)) # <class '__main__.Character'>
print(unit.race) # Human
print(unit.damage) # 40
print(unit.armor) # 33


