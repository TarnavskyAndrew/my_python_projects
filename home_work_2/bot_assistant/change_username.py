from colorama import Fore

def change_username(args, contacts):
    if len(args) != 2:
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Enter old name and new name like: rename old_name new_name"

    old_name, new_name = args

    if not old_name.isalpha() or not new_name.isalpha():
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Names must contain only letters"

    if old_name not in contacts:
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Contact '{old_name}' not found"

    if new_name in contacts:
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Contact '{new_name}' already exists"

    phones = contacts[old_name]  # Зберігаємо телефони старого імені
    
    del contacts[old_name]  # Видаляємо старе ім'я
    
    contacts[new_name] = phones  # Додаємо нове ім'я з цими ж телефонами

    return f"{Fore.GREEN}Name changed from {old_name} to {new_name}.{Fore.RESET}"
