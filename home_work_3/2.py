
import re
from typing import Callable

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    
    pattern = r'\d+\.\d+'
    text_out_num = re.findall(pattern, text)
 
    for i in text_out_num:
        i = float(i)
        # print(f"➡ Генерация i = {i}")
        yield i
        
   
def sum_profit(text: str, func: Callable):
    
    return sum(func(text))
    
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")