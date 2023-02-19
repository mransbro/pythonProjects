import datetime as dt


def main():
    while True:
        try:
            year = int(input("Enter year: "))
        except ValueError:
            print("Sorry i didnt understand that")
            continue

        if year < 1 or year > 9999:
            print("Sorry, your response must be between 1 and 9999.\n")
            continue
        else:
            break

    while True:
        try:
            month = int(input("Enter month: 1-12 "))
        except ValueError:
            print("Sorry i didnt understand that")
            continue

        if month < 1 or month > 12:
            print("Sorry, your response must be between 1 and 12.\n")
            continue
        else:
            break

    cal_text = dt.datetime(year, month, 1).strftime("%B %Y")


if __name__ == "__main__":
    main()
