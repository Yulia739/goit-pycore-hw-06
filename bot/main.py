from parse_input import parse_input
from handlers_func import add_contact, change_contact, show_phone, show_all_contacts
from address_book import AddressBook

def main():
    book = AddressBook()
    """Manages the main command processing cycle"""
    print(f"Welcome to the assistant bot!")
    while True:
        user_input = (
            input(
                """1. hello\n2. add\n3. change\n4. phone\n5. all\n6. exit or close\nEnter a command: """
            )
            .strip()
            .lower()
        )
        parse_res = parse_input(user_input)
        cmd, *args = parse_res
        match cmd:
            case "hello":
                print(f"How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(show_phone(args, book))
            case "all":
                print(show_all_contacts(book))
            case "exit" | "close":
                print(f"Good bye!")
                break
            case _:
                print(f"Invalid command.\n")


if __name__ == "__main__":
    main()
