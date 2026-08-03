# ЗАДАНИЕ 1: Работа с типами данных
stroka = "Привет"
number = 42
float = 3.14
list = [1, 2, 3]
print(type(stroka))
print(type(number))
print(type(float))
print(type(list))

# ЗАДАНИЕ 2: Преобразование регистра строк
text = "python PROGRAMMING"
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())

# ЗАДАНИЕ 3: Удаление пробелов
text_1 = "  Hello World  "
print(text_1.strip())
print(text_1.lstrip())
print(text_1.rstrip())

# ЗАДАНИЕ 4: Разделение и объединение строк
fruits = "яблоко,банан,апельсин,груша"
fruit_list = fruits.split(",")
print(fruit_list)
itog = " | ".join(fruit_list)
print(itog)

# ЗАДАНИЕ 5: Замена подстрок
text = "Я изучаю Python. Python - это круто!"
new_text = text.replace("Python", "Java")
print(new_text)

# ЗАДАНИЕ 6: Поиск и подсчет
text = "Python программирование на Python"
print(text.find("Python"))
print(text.count("Python"))
print(text.find("Java"))

# ЗАДАНИЕ 7: Проверка типа символов
print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())

# ЗАДАНИЕ 8: Срезы строк
text = "Python very good"
print(text[:3])
print(text[-3:])
print(text[::2])
print(text[::-1])

# ЗАДАНИЕ 9: Экранирование символов
print("Он сказал: \"Привет\"")
print("Первая строка\nВторая строка")