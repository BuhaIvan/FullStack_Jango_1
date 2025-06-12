# dict - список пар (ключ: значение)
players = {
    "Carlsen": 2842,
    "Caruana": 2822,
    "Mamedyarov": 2801,
    "Ding": 2797,
    "Giri": 2780
}

players_new = dict(one=1, two=2, three=3)

# Вытянуть значению по ключу
top = players["Carlsen"]
print(f"Top chess player's rating is {top}") # Top chess player's rating is 2842

# Добавить новую пару в словарь
players["So"] = 2781
print(players) # {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyarov': 2801, 'Ding': 2797, 'Giri': 2780, 'So': 2781}

# Что бы удалить запись из словаря нужно использовать del
del players["So"]
print(players) # {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyarov': 2801, 'Ding': 2797, 'Giri': 2780}

# Что бы посмотреть все ключи словаря надо использовать ф-цию keys
print(players.keys()) # dict_keys(['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri'])

# что бы создать список ключей
l = list(players.keys())
print(l) # ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri']

# Получить отсортированный список
print(sorted(players.keys())) # ['Carlsen', 'Caruana', 'Ding', 'Giri', 'Mamedyarov']

# Что бы проверить есть ли ключ в словаре
print("Carlsen" in players) # True
print("Carlsen" not in players) # False
print("Kramnik" not in players) # True

# values() - что бы посмотреть список значений
print(players.values()) # dict_values([2842, 2822, 2801, 2797, 2780])
print(list(players.values())) # [2842, 2822, 2801, 2797, 2780]

# создать копию
players_copy = players.copy()
print(players_copy) # {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyarov': 2801, 'Ding': 2797, 'Giri': 2780}

# как использовать цикл для словаря
# items возвращает список пар ключ: значение
for key, value in players.items():
    print(key, value)

# удалить элемент по ключу можно через pop()
players.pop("Giri")
print(players) # {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyarov': 2801, 'Ding': 2797}

players.popitem()
print(players) # {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyarov': 2801}

# setdefault() - при вызове если не находит элемент то, добавляет заданный ключ, а значение вставляет None
players.setdefault("Karjakin")
print(players) # {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyarov': 2801, 'Karjakin': None}