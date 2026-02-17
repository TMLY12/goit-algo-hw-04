def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Контакт добавлен!"


def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Контакт обновлён!"
    else:
        return "Error: Контакт не найден."


def show_all(contacts):
    if not contacts:
        return "Контакт не найден."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error! Contact not found."


def main():
    contacts = {}
    print("Welcome!")

    while True:
        user_input = input("Enter command: ")
        parts = user_input.split()
        if not parts:
            continue
        command = parts[0].lower()
        args = parts[1:]
        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Unknown command.")
if __name__ == "__main__":
    main()