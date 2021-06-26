# Timothy Schultz
# Professor Hauschild
# CS 4762 Introduction to Cryptography
# for Computer Security
# Project 1
# 6/25/2021

import re

# Class for building a circular list


class Node:

    def __init__(self, char):
        self.char = char
        self.next = None


class CircularList:

    def __init__(self):
        self.head = None

    def add(self, char):
        hold = Node(char)
        temp = self.head
        hold.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = hold
        else:
            hold.next = hold

        self.head = hold


print("Vigenere Cipher\n")

# Prompt user for sentence to encrypt and the key.
sentence = str(input("Enter a sentence to encrypt: "))
key = str(input("Enter a key: "))

# Coverts all alphabetic letters to lower case.
sentence = sentence.lower()
key = key.lower()

# Regular expression that removes all upper case and non alphabetical characters.
regular_expression = re.compile('[^a-za-z]')
sentence = regular_expression.sub('', sentence)
key = regular_expression.sub('', key)

# Convert Sentence and key to lists
sentence = list(sentence)
key = list(key)
difference = list()
sentenceList = CircularList()
index = 0

for x in range(len(sentence)):
    sentenceList.add(sentence[x])

    if index == (len(key) - 1):
        index = 0

    difference.append(ord(key[index]) + ord(sentence[x]))
    index = index + 1

print(difference)
