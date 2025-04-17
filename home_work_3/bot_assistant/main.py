# bot_assistant
from colorama import Fore
from parse_input import parse_input
from add_contact import add_contact
from show_all_contacts import show_all_contacts
from phone_contact import phone_contact
from change_username_phone import change_username_phone
# from load_contacts_from_file import load_contacts_from_file
# from save_contacts_to_file import save_contacts_to_file
# from change_username import change_username



def main():
    contacts = {}
    # FILENAME = "./TASKs/task_4/bot_assistant/contacts.txt"
    # contacts = load_contacts_from_file(FILENAME)    
    
    print(f"{Fore.MAGENTA}Welcome to the assistant bot!{Fore.RESET}")
    

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        # command, *args = parse_input(user_input)
        if not command:
            print(f"{Fore.YELLOW}Empty input. Type a command like 'hello' or 'add'.{Fore.RESET}")            
            continue  # користувач нічого не ввів - пропускаємо

        if command in ["close", "exit"]:
            # save_contacts_to_file(FILENAME, contacts)
            print(f"{Fore.GREEN}Contacts saved. Goodbye, have a nice day!{Fore.RESET}")
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






