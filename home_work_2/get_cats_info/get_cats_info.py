import os
from colorama import Fore

FILENAME = "./home_work_2/get_cats_info/cats_info.txt"

def get_cats_info(path) -> list:
    
    """
    Отримує дані про котів із файлу.
    Повертає список словників: [{"id": id, "name": name, "age": age}]
    """
    
    try:
        if os.path.getsize(path) == 0:   # Перевіряємо чи є дані у файлі
            print(f"{Fore.YELLOW}[WARNING:]{Fore.RESET} The file exists, but there is no data.")
            return []
               
        with open(path, "r", encoding="utf-8") as file:
            cats_list = [] 
            for line in file:
                
                clean_line = line.replace(".", ",")    # Замінюємо крапку на кому всередині рядка
                parts = clean_line.strip().split(",") # Забираємо все зайве і розділити за комою                
               
                if len(parts) == 3:   # Перевіряємо що 3 елементи: id, name, age
                    id, name, age = parts[0].replace(" ", "").strip(), parts[1].strip(), parts[2].strip() # Розпаковуємо список за трьома елементами, прибираємо зайві пробіли
                    cats_list.append({"id": id, "name": name, "age": age})
                else:
                    print(f"{Fore.YELLOW}[WARNING:]{Fore.RESET} Invalid line: -> {line.strip()}")

        if not cats_list:
            print("No data to calculate salary")
            return []
    
        return cats_list

    except (Exception) as e: 
        print(f"{Fore.RED}[ERROR:]{Fore.RESET} {e}")     # Обробка помилки, якщо файлу немає
        return []


cats_info = get_cats_info(FILENAME) 
for cat in cats_info:
    print(cat)
  



    