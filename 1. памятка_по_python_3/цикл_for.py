# цикл for используется для прохождения по итерируемым объектам
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number) # выведет все числа

for number in numbers:
    print(number ** 2) # выведет квадраты чисел из списка

numbers_1 = range(1, 6) # сделать список от 1 до 5
for number in numbers_1:
    print(number)

# вывести четные и нечетные числа
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

# перезаписать существующий список квадратами чисел
numbers_2 = [1, 3, 5, 7, 9]
for i, item in enumerate(numbers_2):
    numbers_2[i] *= item

print(numbers_2)

# выведет каждый символ из строки на новой строчке
name = "John"
for letter in name:
    print(letter)

# если нам не нужна переменная может использовать _
for _ in range(5):
    print("Hello!")


# через for можно работать так же с кортежами
person = ("John", "Silver", 22)
for item in person:
    print(item)

# Распаковка списка кортежей
persons = [("John", 22), ("Bob", 32), ("Dave", 20)]
for (name, age) in persons:
    print(f"{name} is {age} years old")

# Цикл для словарей
players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801)
for item in players:
    print(item) # Получим только ключи

for item in players.items():
    print(item) # Получим список таплов

for k, v in players.items():
    print(f"{k} has rating {v}")

for v in players.values():
    print(v) # Получим только значения

# Вложенные циклы

# find all pairs sum of which equals 0
list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, 3, 5, -2]

pairs = []
for x in list1:
    for y in list2:
        if x + y == 0:
            pairs.append((x, y))

print(pairs)