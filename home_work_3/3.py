import os
from colorama import Fore
from collections import Counter


FILENAME = "./home_work_3/log.txt"


def parse_log_line(line) -> dict:
    
    parts = line.strip().split(" ", 3)  
    if len(parts) == 4: 
        
        date, time_part, level, message = parts
        
        return {
            "date": date,
            "time": time_part,
            "level": level.upper(),
            "message": message
            }
    
    else:
        print(f"{Fore.YELLOW}[WARNING:]{Fore.RESET} Skipped invalid line: -> {Fore.BLUE}{line.strip()}{Fore.RESET}")  
        return None
        
     
def load_logs(file_path) -> list:       
        
    try:    
        if os.path.getsize(file_path) == 0:      # Перевіряємо чи є дані у файлі
            print(f"{Fore.YELLOW}[WARNING:]{Fore.RESET} The file exists, but there is no data.")
            return []    
        
        with open(file_path, "r", encoding="utf-8") as file:
            
            logs = [] 
            for line in file:  
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)  

            if not logs:
                print(f"{Fore.YELLOW}[WARNING:]{Fore.RESET} All lines are invalid. No data to analyze.")
                return [] 
                       
        return logs
    except (Exception) as e: 
        print(f"{Fore.RED}[ERROR:]{Fore.RESET} {e}")     # Обробка помилки, якщо файлу немає
        return []

logs = load_logs(FILENAME)
#print(logs)
for log in logs:
    print(log)  
    
    

def count_logs_by_level(logs) -> dict:
    
    # log_counts = {} 
     
    # for log in logs:
    #     level = log["level"]
    #     if level in log_counts:
    #         log_counts[level] += 1
    #     else:
    #         log_counts[level] = 1
    
    # return log_counts  

    return Counter(log["level"] for log in logs) 

counts = dict(count_logs_by_level(logs)) 
print(counts, type(counts))


def display_log_counts(counts: dict): 

    print() 
    print(f"{Fore.YELLOW}{'Рівень логування':<18}| {'Кількість'}{Fore.RESET}")
    print(f"{'-'*18}|{'-'*11}")
    
    for level, count in counts.items():
        print(f"{level:^18}| {count:^9}")  
    print()       

display_log_counts(counts)


# def filter_logs_by_level(logs: list, level: str) -> list:
    


def main():
       
    logs = load_logs(FILENAME) 
    counts = dict(count_logs_by_level(logs))
    display_log_counts(counts)


if __name__ == "__main__":
    main()


