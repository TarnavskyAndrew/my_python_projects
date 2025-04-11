from colorama import Fore   
     
def save_contacts_to_file(filename, contacts):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for name, phones in contacts.items():
                file.write(f"{name}: {', '.join(phones)}\n")
                
    except (Exception) as e: 
        print(f"{Fore.RED}[ERROR:]{Fore.RESET} {e}")     # Обробка помилки, якщо файлу немає
        return []