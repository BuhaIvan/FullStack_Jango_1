# коллекции - списки
int_list = [1, 2, 3]

# списки могут содержать различные типы данных
mixed_list = [1, 2.0, "str"]

# длину списка можно узнать с помощью метода len()
print(len(mixed_list)) # 3

# к элементу списка можно обратиться п списку
print(mixed_list[1]) # 2.0

# списки поддерживают срезы
print(mixed_list[1:3]) # [2.0, 'str']

# Списки поддерживают конкатенацию
names_1 = ["Ivan", "John", "Sara"]
names_2 = ["Yana", "Koly", "Sanya"]
names = names_1 + names_2
print(names) # ['Ivan', 'John', 'Sara', 'Yana', 'Koly', 'Sanya']

# списки - изменяемые
names[0] = "Liam"
print(names) # ['Liam', 'John', 'Sara', 'Yana', 'Koly', 'Sanya']

# Что бы добавить в список новый элемент надо вызвать метод .append()
names_1.append("William")
names_1.append("James")
print(names_1) # ['Ivan', 'John', 'Sara', 'William', 'James']

# С помощью pop() можно удалить элемент (по индексу или с конца) и так же этот элемент запишется в переменную
some_name = names_1.pop(1)
print(some_name) # John
print(names_1) # ['Ivan', 'Sara', 'William', 'James']

# для сортировки можно использовать метод sort()
names_1.sort()
print(names_1) # ['Ivan', 'James', 'Sara', 'William']

letters = ["ac", "ab", "aa"]
letters.sort()
print(letters) # ['aa', 'ab', 'ac']

# Сортировать можно по ключу
letters = ["abc", "a", "ab"]
letters.sort(key=len)
print(letters) # ['a', 'ab', 'abc']

number_1 = [3, 2, 8, 5, 0, 3, 4, 1, 1]
number_1.sort()
print(number_1) # [0, 1, 1, 2, 3, 3, 4, 5, 8]

# что бы реверсировать список можем и использовать ф-цию ревёрс
number_1.reverse()
print(number_1) # [8, 5, 4, 3, 3, 2, 1, 1, 0] (так как после .sort())

# Вставить элемент по индексу
number_1.insert(1, 22)
print(number_1)

# Получить индекс элемента
print(number_1.index(22)) # 1

# Посчитать кол-во элементов в списке
print(number_1.count(3)) # 2

# Что бы сделать копию списка можно использовать ф-цию copy
number_1_copy = number_1.copy()
print(number_1_copy) # [8, 22, 5, 4, 3, 3, 2, 1, 1, 0]

# Что бы очистить список можно использовать ф-цию clear()
number_1_copy.clear()
print(number_1_copy) # []