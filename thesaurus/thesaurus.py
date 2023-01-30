#!/usr/bin/python3
import json
import sys

with open('./data.json') as f:
    words = json.load(f)

print("""

'Welcome to Michael\'s Thesaurus'

""")


def thesaurus():
    word = input("Please enter a word\n\n")
    word = word.lower()

    try:
        a = (words[word])
    except KeyError:
        print(f'Sorry couldnt find an entry for {word}')
        sys.exit(1)

    for count, value in enumerate(a):
        print(f"{count + 1}. {value}\n")


while True:
    thesaurus()
    cont = input("Would you like to look up another word? yes or no\n")
    while cont.lower() not in ("yes", "no", "y", "n"):
        cont = input("Would you like to look up another word? yes or no\n")
    if cont == "no" or cont == "n":
        break
