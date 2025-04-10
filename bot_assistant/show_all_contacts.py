from colorama import Fore

def show_all_contacts(contacts):
    if not contacts:
        return f"{Fore.YELLOW} No contacts found.{Fore.RESET}"

    result = []
    for name, phones in contacts.items():
        result.append(f"{name}: {', '.join(phones)}")

    return "\n".join(result)
