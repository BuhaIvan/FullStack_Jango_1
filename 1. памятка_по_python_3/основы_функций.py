# ф-ции нужны, что бы не повторять код, а переиспользовать его (ф-цию)
# ф-ция начинается с def name(*args, **kwargs):

def greeting1():
    """
    Info about function
    :return: None
    """
    print("Hello!")

# вызов ф-ции:
greeting1() # Hello!

print(help(greeting1))
# greeting()
#     Info about function
#     :return: None

# ф-ция может принимать аргументы
def print_name(name):
    print(name)

print_name("Elijah") # Elijah

# У аргумента может быть значение по умолчанию
def print_name_1(name="Default"):
    print(name)
print_name_1() # Default

# Ф-ция может возвращать что либо

result = print_name_1()
print(result) # None
print(type(result)) # <class 'NoneType'>

def get_greeting(name):
    return "Hello " + name

greeting = get_greeting("Ivan")
print(greeting) # Hello Ivan

def get_sum(a, b):
    return a + b

result = get_sum(1, 2)
print(result) # 3

def is_adult(age):
    return age >= 18
is_adult = is_adult(20)
print(is_adult) # True

def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("aabaa")) # True
print(is_palindrome("aabaac")) # False

def calc_taxes(p1, p2, p3):
    return sum([p1, p2, p3]) * 0.06

print(calc_taxes(12, 13, 14)) # 2.34

# args - позволяет передать n-ное кол-во элементов
def calc_taxes_args(*args):
    return sum(args) * 0.06

print(calc_taxes_args(1,2,3,4,5))

# kwargs - позволяет передать n-ное кол-во пар ключей
def save_players(**kwargs):
    for k, v in kwargs.items():
        print(f"Player {k} has rating {v}")

save_players(Carlsen=2800, Giri=2780)
# Player Carlsen has rating 2800
# Player Giri has rating 2780

