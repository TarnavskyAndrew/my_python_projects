#>>> 1

""" Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою."""

from datetime import datetime

def get_days_from_today(date):       
    # Перевіряємо вхідний параметри, за необхідності наводимо до одного типу:
    if "." in date or "," in date or "_" in date or " " in date:
        date_string = date.replace(".", "-").replace(",", "-").replace("_", "-").replace(" ", "-")  
                  
    try:  
        start_day = datetime.strptime(date, "%Y-%m-%d").date()  # Перетворимо рядок на об'єкт типу date           
        today = datetime.today().date()     # Отримуємо сьогоднішню дату     
        difference_day = today - start_day  # Обчислюємо різницю у днях
        return difference_day.days  
      
    except ValueError:
        print("Please enter the date in the following format: YYYY-MM-DD")        

result = get_days_from_today("2020-10-09")
print(f"date difference: {result}") # date difference :1636

print()


#>>> 2

"""
Необхідно написати функцію get_numbers_ticket(min, max, quantity), 
яка допоможе генерувати набір унікальних випадкових чисел. 
"""

import random

MIN = 1
MAX = 1000
quantity = random.randint(1, 7)
# print(quantity)

def get_numbers_ticket(min:int=MIN, max:int=MAX, quantity:int=quantity) ->int :
    
    #Перевіряємо, що всі аргументи - цілі числа (int)
    if not all(isinstance(x, int) for x in [min, max, quantity]):
        return ["Error: All arguments must be integers"]   
    
    try:       
        #Перевіряємо, що значення перебувають у допустимих межах
        if min >= MIN and max <= MAX and min <= max and 1 <=  quantity <= max-min:
           range_numb = random.sample(range(min, max), quantity)
           return sorted(range_numb) 
        else:
            return []
    except (TypeError, ValueError) as e:
        return [f"Error {e}"]
    
result = get_numbers_ticket(1, 100, 10)
print(result)

print()


#>>> 3

""" 
Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, 
залишаючи тільки цифри та символ '+' на початку.
"""

import re 

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    
    # Видаляємо всі символи, окрім цифр
    cleaned_number = re.sub(r"\D", "", phone_number)
    # Наводимо номер до міжнародного формату
    if cleaned_number.startswith("380"):
        cleaned_number = "+" + cleaned_number
    else:
        cleaned_number = "+38" + cleaned_number 
        
    return cleaned_number  

fixed_numbers = list(map(normalize_phone, raw_numbers))
print(fixed_numbers)


print("."*150)