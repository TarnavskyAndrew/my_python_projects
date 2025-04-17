
# def parse_input(user_input):
#     cmd, *args = user_input.split()
#     cmd = cmd.strip().lower()
#     return cmd, *args


def parse_input(user_input):           
    parts = user_input.strip().split()
    if not parts:
        return "", []        # якщо користувач введе пусте значення
    cmd, *args = parts
    return cmd.lower(), args   # повертаємо команду та аргументи як список




