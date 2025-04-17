from colorama import Fore
from utils.decorators import input_error

@input_error
def show_all_contacts(contacts):
    if not contacts:
        return f"{Fore.YELLOW} No contacts found.{Fore.RESET}"

    result = []
    for name, phones in contacts.items():
        result.append(f"{Fore.GREEN}>>>{Fore.RESET} {name}: {', '.join(phones)}")

    return "\n".join(result)
