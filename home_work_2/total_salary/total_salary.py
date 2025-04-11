import os

FILENAME = "./home_work_2/total_salary/salary_file.txt"

def total_salary(path: str) -> tuple:
 
    try:
        if os.path.getsize(path) == 0:   # Перевіряємо чи є дані у файлі
            print("The file exists, but there is no data.")
            return []
               
        with open(path, "r", encoding="utf-8") as file:
            salaries = [] 
            for line in file:
                
                clean_line = line.replace(".", ",")    # Замінюємо крапку на кому всередині рядка
                parts = clean_line.strip().split(",")  # Забираємо все зайве і розділити за комою
                
                if len(parts) == 2:      # Перевіряємо, що у рядку є два елементи
                    name, salary = parts[0], parts[1]
                    if salary.isdigit() and int(salary) > 0:    # Перевіряємо, що є зарплата і це число > 0  
                        salaries.append(int(salary))     # Додаємо зарплату до списку
                    else:
                        print(f"WARNING: Incorrect salary in line: {line.strip()}")
                else:
                    print(f"WARNING: Line does not match the format: {line.strip()}")    
        
        if not salaries:
            print("No data to calculate salary")
            return 0, 0
        
        sum_salaries = sum(salaries)
        avg_salaries = sum(salaries) // len(salaries) # Визначаємо суму та середнє значення
           
        return sum_salaries, avg_salaries
        

    except (Exception) as e: 
        return [f"Error: {e}"]     # Обробка помилки, якщо файлу немає
    
result = total_salary(FILENAME)
print(f"sum: {result[0]}, average: {result[1]}")
