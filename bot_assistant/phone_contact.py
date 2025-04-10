from add_contact import add_contact
from colorama import Fore

def phone_contact(args, contacts):
    if not args:
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Enter a name after 'phone'"

    username = args[0]

    if username in contacts:
        return f"{username}: {', '.join(contacts[username])}" #Виводимо username та його телефони
    else:
        return f"{Fore.RED}[ERROR:]{Fore.RESET} Contact not found"