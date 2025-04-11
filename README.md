# My Python Projects 🚀

Welcome to my repository with Python projects!  
Here I learn, practice and improve my coding skills.

---

<details>
<summary>Bot Assistant 🤖 — description and commands</summary>


*A simple console assistant bot written in Python for managing contacts.*

### What bot can do:

- Add contact: `add Name Phone`
- Show phone by name: `phone Name`
- Change phone: `change Name NewPhone`
- Rename contact: `rename OldName NewName`
- Show all contacts: `all`
- Save and exit: `exit` or `close`
- Greeting: `hello`

---

### How it works:

1. Loads contacts from `contacts.txt`
2. After exit (exit or close command), the bot automatically saves all changes to contacts.txt.
3. All data is stored as dictionary:


```python
contacts = {
    "Name": ["380111111111", "380222222222"], 
    "Name": ["380333333333"] 
}

```


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

</details>