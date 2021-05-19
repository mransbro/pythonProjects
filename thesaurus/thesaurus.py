#!/usr/bin/python3
import json

with open('./data.json') as f:
    words=json.load(f)

print("""

'Welcome to Michael\'s Thesaurus'

""")

def thesaurus():
    word = input("Please enter a word\n\n")
    word = word.lower()

    if word in words:
        a = (words[word])
    elif word.capitalize() in words:
        word = word.capitalize()
        a = (words[word])
    elif word.upper() in words:
        word = word.upper()
        a = (words[word])
    else:
        print(f'\nSorry couldnt find an entry for {word}')
        quit()


    for count, value in enumerate(a):
        print(f"{count + 1}. {value}\n")


while True:
    thesaurus()
    cont = input("Would you like to look up another word? yes or no\n")
    while cont.lower() not in ("yes", "no", "y", "n"):
        cont = input("Would you like to look up another word? yes or no\n")
    if cont == "no" or cont == "n":
        break