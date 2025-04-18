
# Декоратор для обробки помилок користувача під час введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return inner

# Функція для розбору введення користувача на команду та аргументи
def parse_input(user_input):
    parts = user_input.strip().split()  
    if not parts:
        return "", []  
    cmd = parts[0].lower()  
    args = parts[1:]  
    return cmd, args

# Обробка команди "add": додає новий контакт
@input_error
def add_contact(args, contacts):
    name, phone = args
    if not phone.isdigit():
        return "Phone number must contain only digits."
    contacts[name] = phone  
    return "Contact added."

# Обробка команди "change": змінює номер телефону для існуючого контакту
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return f"Contact '{name}' not found. Use 'add' to create a new contact."
    if not phone.isdigit():
        return "Phone number must contain only digits."

    contacts[name] = phone  
    return "Contact updated."

# Обробка команди "phone": показує номер телефону за ім'ям
@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]  

# Обробка команди "all": показує всі збережені контакти
def show_all(contacts):
    if not contacts:
        return "No contacts saved."  
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")  
    return "\n".join(result)  

# Обробка команди "help": виводить усі доступні команди
def show_help():
    return (
        "Available commands:\n"
        "  hello           - Greet the bot\n"
        "  add <name> <phone>     - Add a new contact\n"
        "  change <name> <phone>  - Change an existing contact's phone number\n"
        "  phone <name>     - Show the phone number for a contact\n"
        "  all              - Show all contacts\n"
        "  help             - Show this help message\n"
        "  close / exit     - Exit the assistant"
    )

# Основна функція, яка запускає бота
def main():
    contacts = {}  
    print("Welcome to the assistant bot!")  
    while True:
        user_input = input("Enter a command: ")  
        if not user_input.strip():
            continue  

        command, args = parse_input(user_input)  
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "phone":
            print(show_phone(args, contacts))
        
        elif command == "all":
            print(show_all(contacts))
        
        elif command == "help":
            print(show_help())
        
        else:
            print("Invalid command. Type 'help' to see available commands.")

# Запуск бота
if __name__ == "__main__":
    main()

