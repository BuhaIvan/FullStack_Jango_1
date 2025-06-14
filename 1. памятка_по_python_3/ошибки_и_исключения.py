# def divide(a, b):
#     return a / b
#
# print(divide(4, 2)) # 2
# print(divide(4, 0)) # Error ZeroDivisionError: division by zero

def divide_with_0(a, b):
    try:
        result = a / b
        print("Result calculated")
        return result
    except ZeroDivisionError as ex: # обработка для деления на 0
        print(f"an error occured: {ex}")
    except TypeError as ex:
        print(f"use the correct data: {ex}")
    except: # обработает все остальыне ошибки
        print("unknown error!!")

divide_with_0(1, "asd")

# Пример для файла (например нам надо открыть файл, а после этого его закрыть). finally отработает в любом случае после try
file = None
try:
    file = open(r"C:\tmp\aaaaaa.txt")
    data = file.read()
except FileNotFoundError as ex:
    print(f"Error has occured. Description: {ex.strerror}")
finally:
    print("finally block")
    if file:
        file.close()

print("code after block")

def get_int():
    while True:
        try:
            reply = int(input("Enter a number: "))
            return reply
        except:
            print("Not a number! Try again")
            continue

number = get_int()
