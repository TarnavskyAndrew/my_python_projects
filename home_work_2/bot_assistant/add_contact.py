
from colorama import Fore


def add_contact(args, contacts):
    if len(args) != 2:
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Enter your name and phone number separated by spaces: -> 'change Name number'"

    name, phone = args

    if not name.isalpha():   # Перевіряємо, що ім'я тільки літери
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Name must contain only letters"

    if not phone.isdigit():  # Перевіряємо, що телефон тільки цифри
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Phone must contain only numbers"

    # Перевіряємо, якщо ім'я вже є – не перезаписуємо, а додаємо до списку телефонів
    if name in contacts:
        contacts[name].append(phone)
    else:
        contacts[name] = [phone]

    return f"{Fore.GREEN}Contact added.{Fore.RESET}"





