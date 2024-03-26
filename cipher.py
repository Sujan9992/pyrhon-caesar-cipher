def cipher(choice: str, shift: int, message: str) -> None:
    result: str = ""
    if choice == "decode":
        shift = -shift

    for char in message:
        if char.isalpha():
            offset: int = 65 if char.isupper() else 97
            shifted: str = chr((ord(char) - offset + shift) % 26 + offset)
            result += shifted
        else:
            result += char

    print(result)


def check_choice(choice: str) -> bool:
    return choice == "encode" or choice == "decode"
