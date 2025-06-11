# Строки - используются чаще всего

# Строки могут быть в одинарных и двойных ковычках
a = "String"
a1 = 'String'

# Если в самом тексте используются ковычки, то можно использовать для строки ковычки другого типа
b = "I'm a programmer"

# Escape последовательность. \ используется для экранирования
c = "I'm Ivan and I'm a \"strong\" programmer"
print(c) # I'm Ivan and I'm a "strong" programmer

# Если внутри строки нужно прописать обратный слеш
d = "c:\\Users\\MySpace"
print(d) # c:\Users\MySpace
# Так же можно использовать символ r
d1 = r"c:\Users\MySpace"
print(d1)

# Перенос на следующую строку делается с помощью \n
e = "I'm Ivan and \nI'm a \"strong\" programmer"
print(e)
# I'm Ivan and
# I'm a "strong" programmer

# \t - используется для табуляции

# str() - конструктор строки
hello = str("Hello, my name is Ivan!")
print(hello) # Hello

# Строки индексируемые (можно обратиться к элементу по индексу)
print(hello[1]) # e
print(hello[-1]) # o
# print(hello[11]) # IndexError: string index out of range

# Строки не изменяемые
# hello[0] = "h" # TypeError: 'str' object does not support item assignment

# Срез - подстрока. Позволяет вывести часть строки (первое число начальный индекс, второе - конечный символ, третье -
# шаг)
print(hello[2:]) # llo, my name is Ivan!
print(hello[3:]) # lo, my name is Ivan!
print(hello[3:8]) # lo, m
print(hello[3:11:2]) # l,m

# Конкатенация строк
print("My name is" + " " + "Ivan") # My name is Ivan

hello = "Hello"
world = "world"
print(hello + " " + world) # Hello world
print("%s %s" % (hello, world)) # Hello world
print("{} {}".format(hello, world)) # Hello world
print(f"{hello} {world}") # Hello world

# Дублицирование
print("a" * 7) # aaaaaaa