import rich
import string


def main():
    letters = list(string.ascii_lowercase)

    while True:
        try: 
            answer = str(input("Do you want to (e)ncrypt or (d)ecrypt?\n"))
        except ValueError:
            print("Sorry i didnt understand that")
            continue
        
        if answer.lower().startswith("e"):
            mode = "enrypt"
            continue
        elif answer.lower().startswith("d"):
            mode = "decrypt"
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

    for num, char in enumerate(temp_list):
        if char.isalpha():
            if mode == "encrypt":
                position = num + key
            elif mode == "decrypt":
                position = num - key

            if position >= 25:
                position = position - 25
            temp_list[num] = letters[position]

    output = ''.join(temp_list)

    rich.print(f"\n{output}")


if __name__ == "__main__":
    main()
