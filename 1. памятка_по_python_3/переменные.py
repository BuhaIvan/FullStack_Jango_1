# присвоили переменной x 3
from math import sqrt

x = 3
print(x) # 3

# переприсвоили переменную x
x = 5

y = 2
print(x + y) # 7
print(x + x) # 10
print(y + y) # 4

# переприсвоили х после сложения
x = x + x
print(x) # 10

# что бы проверить тип переменной может использовать type()
print(type(x)) # int

x = 3.14
print(type(x)) # float

b = "abs"
print(type(b)) # str

# print(x + b) # error

# получаем площадь треугольника
a = 10
b = 5
c = 7
p = (a + b + c) / 2

area = sqrt(p*(p-a)*(p-b)*(p-c))

print(p)
print(area)