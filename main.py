# Timothy Schultz
# Professor Hauschild
# CS 4762 Introduction to Cryptography
# for Computer Security
# Project 1
# 6/25/2021

import re

# *************************************************************************************************************

character_dict = {
    "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
    "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22,
    "x": 23, "y": 24, "z": 25
}

character_dict_cipher = {
    0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l",
    12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w",
    23: "x", 24: "y", 25: "z"
}

# *************************************************************************************************************


def plain_to_cipher():
    # Prompt user for sentence to encrypt and the key.
    sentence = str(input("Enter a Plain Text to encrypt: "))
    key = str(input("Enter a key: "))

    # Changes string to lowercase.
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
    index = 0
    cipher_sentence = ""

    for x in range(len(sentence)):
        if index == len(key):
            index = 0

        if character_dict[key[index]] == character_dict[sentence[x]]:
            difference.append(0)
        elif (character_dict[key[index]] + character_dict[sentence[x]]) > 25:
            difference.append(character_dict[key[index]] + character_dict[sentence[x]] - 25)
        else:
            difference.append(character_dict[key[index]] + character_dict[sentence[x]])

        index = index + 1
        cipher_sentence += character_dict_cipher[difference[x]]

    print("Cipher Text: " + cipher_sentence)

# *************************************************************************************************************


def cipher_to_plain():
    # Prompt user for sentence to encrypt and the key.
    cipher_text = str(input("Enter a Cipher Text to decrypt: "))
    key = str(input("Enter a key: "))

    # Changes string to lowercase.
    cipher_txt = cipher_text.lower()
    key = key.lower()

    # Regular expression that removes all upper case and non alphabetical characters.
    regular_expression = re.compile('[^a-za-z]')
    cipher_text = regular_expression.sub('', cipher_txt)
    key = regular_expression.sub('', key)

    # Convert Sentence and key to lists
    cipher_text = list(cipher_text)
    key = list(key)
    difference = list()
    index = 0
    plain_sentence = ""

    for x in range(len(cipher_text)):
        if index == len(key):
            index = 0

        if character_dict[key[index]] == character_dict[cipher_text[x]]:
            difference.append(0)
        elif (character_dict[cipher_text[x]] - character_dict[key[index]]) < 0:
            difference.append(character_dict[cipher_text[x]] - character_dict[key[index]] + 25)
        else:
            difference.append(character_dict[cipher_text[x]] - character_dict[key[index]])

        index = index + 1
        plain_sentence += character_dict_cipher[difference[x]]

    print("Plain Text: " + plain_sentence)

# *************************************************************************************************************

print("Project 1: Vigenere Cipher\n")

while True:
    print("Select an option: ")
    print("1. Task One: Encryption")
    print("2. Task One: Decryption")
    print("3. Quit Program\n")

    answer = int(input("Option: "))
    print("")

    if answer == 1:
        plain_to_cipher()
        print("")
    elif answer == 2:
        cipher_to_plain()
        print("")
    elif answer == 3:
        break
    else:
        print("Incorrect option try again.\n")
