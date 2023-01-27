import rich
import string

def main():
    letters = {}
    for num, letter in enumerate(string.ascii_lowercase):
        letters[num] = letter
        
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
            key = int(input("Please enter the key (0 to 25)?\n"))
        except ValueError:
            print("Sorry i didnt understand that")

        if key < 0 or key > 25:
            print("Sorry, your response must be between 0 and 25.\n")
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
    
    temp_list = [letters[key] for l in list(text) if l.isalpha]


if __name__ == "__main__":
    main() 