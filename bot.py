def hello_command():
    return "How can I help you?"


def add_contact_command(username, phone, contacts):
    contacts[username] = phone
    return f"Contact {username} with phone number {phone} added successfully."


def change_phone_command(username, phone, contacts):
    if username in contacts:
        contacts[username] = phone
        return f"Phone number for contact {username} changed successfully."
    else:
        return f"Contact {username} does not exist."


def phone_command(username, contacts):
    if username in contacts:
        return f"The phone number for contact {username} is {contacts[username]}."
    else:
        return f"Contact {username} does not exist."


def all_command(contacts):
    if contacts:
        return "\n".join([f"{username}: {phone}" for username, phone in contacts.items()])
    else:
        return "No contacts found."


def bot():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print(hello_command())
        elif command.startswith("add"):
            _, username, phone = command.split(maxsplit=2)
            print(add_contact_command(username, phone, contacts))
        elif command.startswith("change"):
            _, username, phone = command.split(maxsplit=2)
            print(change_phone_command(username, phone, contacts))
        elif command.startswith("phone"):
            _, username = command.split(maxsplit=1)
            print(phone_command(username, contacts))
        elif command == "all":
            print(all_command(contacts))
        else:
            print("Invalid command. Please try again.")


bot()
