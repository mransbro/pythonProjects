import rich
import string


def main():
    letters = list(string.ascii_lowercase)

    while True:
        valid = ["e", "encrypt", "d", "decrypt"]
        purpose = input("Do you want to (e)ncrypt or (d)ecrypt?\n")
        if purpose.lower() not in valid:
            print("Sorry i didnt understand that")
            continue
        else:
            break

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

    temp_list = list(text)
    
    if purpose == "e":
        for num, char in enumerate(temp_list):
            if char.isalpha():
                pos = num + key
                if pos > 24:
                    pos = pos - 24
                temp_list[num] = letters[pos]
    
    if purpose == "d":
        for num, char in enumerate(temp_list):
            if char.isalpha():
                pos = num - key
                if pos > 24:
                    pos = pos - 24
                temp_list[num] = letters[pos]

    output = ''.join(temp_list)

    rich.print(f"\n{output}")


if __name__ == "__main__":
    main()
