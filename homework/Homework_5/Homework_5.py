# ЗАДАНИЕ 1: Добавление элементов в список
fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")

print(fruits)

# ЗАДАНИЕ 2: Удаление элементов из списка

fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
last_fruit = fruits.pop()

print(fruits)
print(last_fruit)

# ЗАДАНИЕ 3: Поиск элементов в списке
fruits = ["яблоко", "банан", "апельсин", "банан"]
index_banana = fruits.index("банан")
count_banana = fruits.count("банан")

print(index_banana)
print(count_banana)

# ЗАДАНИЕ 4: Сортировка и реверс списка
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
numbers.reverse()

print(numbers)
