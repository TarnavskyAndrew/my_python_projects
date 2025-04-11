
# Bot Assistant 🤖

A simple console assistant bot written in Python for managing contacts.

---

## Features:

- Add contact: `add Name Phone`
- Show phone by name: `phone Name`
- Change phone number: `change Name NewPhone`
- Rename contact: `rename OldName NewName`
- Show all contacts: `all`
- Save and exit: `exit`  or  `close`
- Greeting: `hello`

---

## How it works:

1. Loads contacts from `contacts.txt` at startup.

2. After using exit or close, the bot automatically saves all changes to `contacts.txt`.

3. All contacts are stored as a Python dictionary:

```python
contacts = {
    "Name": ["380111111111", "380222222222"],
    "Name": ["380333333333"]
}

```


### Example of usage:

Enter a command:  `add Name 380111111111`  ->  
`Contact added.`

Enter a command:  `phone Name`  ->  
`Name: 380111111111`

Enter a command:  `all`  ->  
`Name: 380111111111`

Enter a command:  `exit`  ->  
`Contacts saved. Good bye!`


---


## Project status 🛠️

The project is in progress and will be improved.

### Planned features:
- Delete contact
- Search contact by part of the name
- Validation of phone number format
- Support saving data in JSON
- Auto-formatting phone numbers
- Sorting contacts
- Interface improvements

Stay tuned 😉

---

## Project structure:

```python
bot_assistant/
│
├── main.py
├── add_contact.py
├── change_username_phone.py
├── phone_contact.py
├── show_all_contacts.py
├── load_contacts_from_file.py
├── save_contacts_to_file.py
└── contacts.txt
```


### Run the bot:

`python main.py`


---


### Author:

Created by Tarnavsky Andrew

GitHub: https://github.com/TarnavskyAndrew/my_project_python_git