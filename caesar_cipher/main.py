import rich
import string


def main():
    letters = string.ascii_lowercase

    while True:
        try:
            answer = str(input("Do you want to (e)ncrypt or (d)ecrypt?\n"))
        except ValueError:
            print("Sorry i didnt understand that")
            continue

        if answer.lower().startswith("e"):
            mode = "encrypt"
            break
        elif answer.lower().startswith("d"):
            mode = "decrypt"
            break
        else:
            continue

    while True:
        try:
            key = int(input("Please enter the key (1 to 25)?\n"))
        except ValueError:
            print("Sorry i didnt understand that")
            continue

        if key < 0 or key > 25:
            print("Sorry, your response must be between 1 and 25.\n")
            continue
        else:
            break

    while True:
        text = input("Enter the text to encrypt?\n")
        if not text.isalpha:
            print("Sorry letters only please.")
            continue
        else:
            break

    output = ""

    for char in text:
        if char.isalpha():
            num = letters.find(char)
            if mode == "encrypt":
                num = num + key
            elif mode == "decrypt":
                num = num - key

            if num >= 25:
                num = num - 25

            output = output + letters[num]
        else:
            output = output + char

    rich.print(f"\n{output}")


if __name__ == "__main__":
    main()
