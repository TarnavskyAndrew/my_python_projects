# bot_assistant
from parse_input import parse_input
from add_contact import add_contact
from show_all_contacts import show_all_contacts
from phone_contact import phone_contact
from change_username_phone import change_username_phone
# from change_username import change_username
from colorama import Fore

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":            
            print(add_contact(args, contacts)) 
        elif command == "change":            
            print(change_username_phone(args, contacts))    
        elif command == "all":
            print(show_all_contacts(contacts))
        elif command == "phone":            
            print(phone_contact(args, contacts))
        # elif command == "rename":
        #     print(change_username(args, contacts))    
                    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()







# f"{name}: {', '.join(phones)}"   
# Что такое .join() ?
# Это метод строки, который объединяет элементы списка в одну строку через указанный разделитель.
# phones = ["380111111111", "380222222222"] -> 380111111111, 380222222222



    for name, phones in contacts.items():
        print(f"{name}: {', '.join(phones)}")


#   add dsfdf 23423









# "./TASKs/task_4/total_salary/salary_file.txt"

# from data import load_data, clean_data
# from calculate_salary import calculate_salary
# from pathlib import Path