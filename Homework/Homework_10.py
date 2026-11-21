
# ЗАДАНИЕ 1: Функции и условия

# 1. Функция calculate_total(price, tax_percent)


def calculate_total(price, tax_percent):
    if tax_percent > 20 or price < 0:
        return "Ошибка: некорректная цена или налог"

    total = price + (price * tax_percent / 100)
    return total


print(calculate_total(1000, 10))
print(calculate_total(1000, 25))
print(calculate_total(-100, 10))


# 2. Функция get_level(points)


def get_level(points):
    if points >= 100:
        return "Эксперт"
    elif points >= 50:
        return "Продвинутый"
    elif points >= 20:
        return "Начинающий"
    else:
        return "Новичок"


print(get_level(120))
print(get_level(70))
print(get_level(30))
print(get_level(10))


# ЗАДАНИЕ 2: Функции с условиями и match/case

# 1. Функция process_status(status)


def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"


print(process_status("active"))
print(process_status("inactive"))
print(process_status("pending"))
print(process_status("blocked"))
print(process_status("unknown"))
