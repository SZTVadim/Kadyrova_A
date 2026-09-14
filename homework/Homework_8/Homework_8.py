# ЗАДАНИЕ 1: Список и list comprehension

temps = [18, 22, -3, 25, 19, -1, 21]
new_temps = [x * 9/5 + 32 for x in temps]
print(new_temps)

# ЗАДАНИЕ 2: Словарь и dict comprehension

users = {
     "ivan": "qwerty",
     "maria": "12345",
     "petr": "admin",
     "anna": "pass",
     "guest": "guest"
 }
dictusers = {x: len(x) for x in users}
print(dictusers)

# ЗАДАНИЕ 3: Кортеж и tuple(...)

scores = (10, 7, 0, 9, 8, 5)
new_scores = tuple(x * 1.1 for x in scores)
print(new_scores)
