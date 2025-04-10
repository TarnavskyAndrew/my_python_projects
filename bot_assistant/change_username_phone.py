# from add_contact import add_contact
from colorama import Fore

def change_username_phone(args, contacts):
    
    if len(args) != 2:
        return print(f"{Fore.RED}[ERROR:]{Fore.RESET} Enter your name and phone number separated by spaces: -> 'change Name number'")
    
    name, phone = args

    if not name.isalpha():   # Перевіряємо, що ім'я тільки літери
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Name must contain only letters"

    if not phone.isdigit():  # Перевіряємо, що телефон тільки цифри
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Phone must contain only numbers"

    # Перевіряємо, якщо ім'я вже є – не перезаписуємо, а додаємо до списку телефонів
    if name in contacts:
        contacts[name] = [phone]  # Замінюємо телефони на новий список із 1 телефоном
        return f"{Fore.GREEN}Phone number changed for {name}.{Fore.RESET}"
    else:
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Contact '{name}' not found"


    
