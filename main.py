import re

# Ввод строки от пользователя
input_string = input("Введите строку: ")

# Используем регулярное выражение для поиска цифр
digits = re.findall(r'\d', input_string)

# Выводим найденные цифры
print("Найденные цифры:", ''.join(digits))