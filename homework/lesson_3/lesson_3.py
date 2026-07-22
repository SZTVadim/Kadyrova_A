"Изучаем GIT"

"Азы Python"

a = 1
b = 222
c = b
n = 222
list_1 = [1, 2, 3]
list_2 = list_1
list_2.append(4)
# print(a)
# print(b)
# print(c)
# print("=" * 50)
# print(id(a))
# print(id(b))
# print(id(c))

# print(list_1)
# print(list_2)
# d = a + b
# print(b == a)
# print(b == c)
# print(b != c)
# print(b != a)

# a += 5
# print(a)
# a -= 55
# print(a)
# Пример для and
# s = 64
# if s > 18 and s < 65:
#     print(True)
# else:
#     print(False)


# Пример для or

name = "Petya"

# if "A" in name or "F" in name:
#     print(True)
# else:
#     print(False)

# Пример для not
# if "A" not in name or "F" not in name:
#     print(True)
# else:
#     print(False)

# list_3 = [1, 2, 3]
# print(c is b)
# print(id(list_1))
# print(id(list_3))
a = "False"
b = "True"
if "а" in a:
    print("Это выполнится")
elif b:
    print("a = False, утверждение не истинноFalse, "
          "утверждение не истинноFalse, утверждение "
          "не истинноFalse, утверждение не истинноFalse,"
          " утверждение не истинноFalse, утверждение не истинно")
    if b:
        print("b = True")

"""Мы можем 
сюда написать 
очень 
длинный 
текст"""
# Домашнее задание

name = "Анастасия"
city = "Москва"

print(name)
print(city)

# На какую ячейку памяти ссылается переменная name
print(id(name))

# Тип данных переменной city
print(type(city))