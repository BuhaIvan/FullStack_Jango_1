# Результатом сравнения может быть True of False

result = 2 > 1
print(result) # True

# оператор больше >
print(2 > 2) # False
print(2 >= 2) # True
print(3 >= 2) # True
print(3 >= 4) # False

# оператор меньше <
print(2 < 3) # True
print(3 < 2) # False
print(3 <= 3) # True
print(3 <= 2) # False
print(3 <= 4) # True

# оператор равенства
print(1 == 1) # True
print(1 == 2) # False

# оператор неравенства
print(1 != 1) # False
print(1 != 2) # True

# сравнение строк
print("srt" == "str") # True
print("str" == "another str") # False
print("Str" == "str") # False

# для сравнения строк их лучше привести к одному регистру
x = "str"
y = "Str"
print(x.lower() == y.lower()) # True

# цепочки сравнения
print(1 < 2 < 3) # True

# логический оператор и
print(1 < 2 and 2 < 3) # True
print(1 > 2 and 2 < 3) # False

# логический оператор или
print(1 > 2 or 2 < 3) # True
print(1 > 2 or 2 > 3) # False

# отрицание
is_admin = False
if not is_admin:
    print("not an admin") # not an admin

if is_admin == False:
    print("not an admin") # not an admin