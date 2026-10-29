
# ЗАДАНИЕ 1

fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")

# ЗАДАНИЕ 2

fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
last_fruit = fruits.pop()

# ЗАДАНИЕ 3

fruits = ["яблоко", "банан", "апельсин", "банан"]
banana_index = fruits.index("банан")
banana_count = fruits.count("банан")


# ЗАДАНИЕ 4

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
numbers.reverse()
print(numbers)


# ЗАДАНИЕ 5

cubes = [number ** 3 for number in range(1, 9)]
min_cube = min(cubes)
max_cube = max(cubes)
print(min_cube)
print(max_cube)


# ЗАДАНИЕ 6

numbers = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
numbers_greater_10 = [number for number in numbers if number > 10]
total = sum(numbers_greater_10)
print(total)


# ЗАДАНИЕ 7

cities = ["москва", "санкт-петербург", "казань"]
capitalized_cities = [city.title() for city in cities]
print(capitalized_cities)
