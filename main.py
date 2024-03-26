from cipher import check_choice, cipher


def main() -> None:
    continue_order: bool = True
    while continue_order:
        choice: str = input(
            "Type encode to encrypt the message or decode to decrypt:\n"
        ).lower()

        if not check_choice(choice):
            print("Invalid input. Try again.")
            continue

        while True:
            try:
                shift: int = int(input("Type number of shifts:\n"))
                break
            except ValueError:
                print("Invalid input. Try again.")
                continue

        message: str = input("Type your message:\n")

        cipher(choice, shift, message)

        restart: str = input("Type yes to restart:\n").lower()

        if restart != "yes":
            continue_order = False


if __name__ == "__main__":
    main()
