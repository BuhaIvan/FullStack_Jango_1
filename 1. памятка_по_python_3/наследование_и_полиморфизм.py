import math


class Shape:
    def __init__(self):
        print("Shape created")

    def draw(self):
        print("Drawing a shape")

    def area(self):
        print("Calc area")

    def perimeter(self):
        print("Cals perimeter")

    # Этот метод невозможно вызвать из у объектов классов наследников
    def some_method(self):
        raise NotImplementedError("Can't instantiate an abstract class")

shape = Shape() # Shape created

# Класс Rectangle наследуется от Shape
class Rectangle(Shape):

    def __init__(self, width, height):
        Shape.__init__(self)

        self.width = width
        self.height = height

        print("Rectangle created")

    # в классе наследнике можно переопределить методы базового класса
    def perimeter(self):
        return 2*(self.width + self.height)

    def draw(self):
        print(f"Drawing rectangle with width={self.width} and height={self.height}")

rect = Rectangle(10, 15) # Shape created # Rectangle created

# В классе наследнике можно вызывать методы родительского класса
rect.area() # Calc area

# если метод был переопределён, то он будет вызываться из текущего класса, а не родительского
print(rect.perimeter()) # 50

class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self)

        self.a = a
        self.b = b
        self.c = c

        print("Triangle created")

    def draw(self):
        print(f"Drawing triangle with sides={self.a}, {self.b}, {self.c}")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s*(s - self.a)*(s - self.b)*(s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

triangle = Triangle(10, 10, 10)
# Shape created
# Triangle created

triangle.draw() # Drawing triangle with sides=10, 10, 10
print(triangle.area()) # 43.30127018922193
print(triangle.perimeter()) # 30

# полиморфизм - все классы имеют одинаковые методы
# Мы можем вызвать все общие методы для разных экземпляров

for our_shape in [rect, triangle]:
    our_shape.draw()
# Drawing rectangle with width=10 and height=15
# Drawing triangle with sides=10, 10, 10
# Для использования полиморфизма в пайтоне наследование не обязательно. Главное, что бы несколько классов имели
# одинаковые методы и одинаковую сигнатуру