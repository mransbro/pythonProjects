#!/usr/bin/python3
import json

with open('./data.json') as f:
    words=json.load(f)

print('')
print('')
print('Welcome to Michael\'s Thesaurus')
print('Please enter a word')
print('')
print('')
word = input('')

print (words[word])