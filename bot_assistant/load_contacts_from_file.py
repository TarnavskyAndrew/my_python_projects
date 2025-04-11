from colorama import Fore


def load_contacts_from_file(filename):
    contacts = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if ": " in line:  # Проверяем, что в строке есть разделитель
                    name, phones = line.strip().split(": ")
                    contacts[name] = phones.split(", ")
                else:
                    print(f"{Fore.YELLOW}[WARNING:]{Fore.RESET} Invalid line: -> {line.strip()}")
    except FileNotFoundError:
        print(f"{Fore.BLUE}[INFO] {Fore.RESET} File not found. Starting with empty contacts.")
 

    return contacts