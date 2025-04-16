
# Декоратор для обробки помилок користувача під час введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            # Помилка, якщо ім'я не знайдено в словнику контактів
            return "Error: Contact not found."
        except ValueError:
            # Помилка, якщо не передано обидва значення: ім'я і номер
            return "Give me name and phone please."
        except IndexError:
            # Помилка, якщо не передано жодного аргументу
            return "Enter the argument for the command"
    return inner

# Функція для розбору введення користувача на команду та аргументи
def parse_input(user_input):
    parts = user_input.strip().split()  # Розбиває рядок на слова
    if not parts:
        return "", []  # Повертає пусту команду, якщо рядок був пустим
    cmd = parts[0].lower()  # Перше слово — це команда
    args = parts[1:]  # Решта — це аргументи
    return cmd, args

# Обробка команди "add": додає новий контакт
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError  # Якщо немає 2 аргументів — викликає ValueError
    name, phone = args
    contacts[name] = phone  # Додає запис до словника контактів
    return "Contact added."

# Обробка команди "change": змінює номер телефону для існуючого контакту
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError  # Якщо контакту не існує — помилка KeyError
    contacts[name] = phone  # Оновлює номер
    return "Contact updated."

# Обробка команди "phone": показує номер телефону за ім'ям
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]  # Повертає номер телефону

# Обробка команди "all": показує всі збережені контакти
def show_all(contacts):
    if not contacts:
        return "No contacts saved."  # Якщо контактів нема
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")  # Формує список усіх контактів
    return "\n".join(result)  # Об'єднує список у рядок для виводу

# Основна функція, яка запускає бота
def main():
    contacts = {}  # Словник для збереження контактів
    print("Welcome to the assistant bot!")  # Привітання
    while True:
        user_input = input("Enter a command: ")  # Отримання вводу
        if not user_input.strip():
            continue  # Ігнорування пустого рядка

        command, args = parse_input(user_input)  # Розбір команди

        # Команда виходу
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # Команда привітання
        elif command == "hello":
            print("How can I help you?")

        # Команда додавання контакту
        elif command == "add":
            print(add_contact(args, contacts))

        # Команда зміни номера
        elif command == "change":
            print(change_contact(args, contacts))

        # Команда перегляду номера за ім’ям
        elif command == "phone":
            print(show_phone(args, contacts))

        # Команда перегляду всіх контактів
        elif command == "all":
            print(show_all(contacts))

        # Якщо команда не розпізнана
        else:
            print("Invalid command.")

# Запуск бота
if __name__ == "__main__":
    main()




