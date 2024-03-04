alphabets: list[str] = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def cipher(
    choice: str, shift: int, message: list[str], alphabets: list[str] = alphabets
) -> None:
    shiftedAlphabets: list[str] = []
    result: list[str] = []

    if shift > 26:
        shift = shift % 26

    for i in range(shift, len(alphabets)):
        shiftedAlphabets.append(alphabets[i])

    for j in range(shift):
        shiftedAlphabets.append(alphabets[j])

    while len(result) != len(message):
        if choice == "encode":
            for letter in message:
                position = alphabets.index(letter)
                result.append(shiftedAlphabets[position])
        elif choice == "decode":
            for letter in message:
                position = shiftedAlphabets.index(letter)
                result.append(alphabets[position])

    print("Result: ", "".join(result))


def check_choice(choice: str) -> bool:
    return choice == "encode" or choice == "decode"
