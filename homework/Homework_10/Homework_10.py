# ЗАДАНИЕ 1: Распаковка списка и слияние
statuses = ["queued", "running", "testing", "deploy", "done"]
# 1.
first, *middle, last = statuses

# 2.
newlist = [*middle, "failed", "skipped"]

# 3.
print(first)
print(last)
print(newlist)

# ЗАДАНИЕ 2: Словарь, слияние и вызов функции
browser = {"browser": "chrome", "timeout": 3000}
options = {"headless": True, "timeout": 5000}


def start_session(browser, timeout, headless):
    return f"{browser}, timeout={timeout}, headless={headless}"


# 1.
config = {**browser, **options}

# 2.
result = start_session(**config)

# 3. Выведите config и результат функции
print(config)
print(result)
