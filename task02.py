"""
Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати 
відповідно до введеної команди.
У цій домашній роботі зосередимося на інтерфейсі самого бота.  Найпростіший і найзручніший на початковому етапі розробки 
інтерфейс - це консольний застосунок CLI (Command Line Interface). CLI достатньо просто реалізувати. Будь-який CLI 
складається з трьох основних елементів:
    -> Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та 
    модифікаторів команд.
    -> Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
    -> Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві 
    відповіді від функції - handler-а.
На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, 
змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, 
скористаємося словником. У словнику будемо зберігати ім'я користувача як ключ і номер телефону як значення.
"""

phonebook = {}

def add_contact(name, phone):
    phonebook[name] = phone
    print("Contact added.")

def find_contact(name):
    phone = phonebook.get(name)
    if phone:
        print(f'Номер телефону {name}: {phone}')
    else:
        print(f'Контакт {name} не знайдено')

def update_contact(name, phone):
    if name in phonebook:
        phonebook[name] = phone
        print("Contact updated.")
    else:
        print(f'Контакт {name} не знайдено')

def list_contacts():
    for name, phone in phonebook.items():
        print(f'{name}: {phone}')

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add" and len(args) == 2:
            add_contact(*args)

        elif command == "change" and len(args) == 2:
            update_contact(*args)

        elif command == "phone" and len(args) == 1:
            find_contact(*args)

        elif command == "all":
            list_contacts()

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
