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

# Function that prompts user for two strings and encrypts the first string with the second string using Vigenere
# cipher. First string is the plain text and function ignores all non-alphabetic characters. All uppercase letters
# are converted to lower case. The second string is the key and can be 1 or more in length.


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
    sentence1 = list(sentence)
    key1 = list(key)
    difference = list()
    index = 0
    cipher_sentence = ""

    for x in range(len(sentence)):
        if index == len(key):
            index = 0

        if character_dict[key1[index]] == character_dict[sentence1[x]]:
            difference.append(0)
        elif (character_dict[key1[index]] + character_dict[sentence1[x]]) > 25:
            difference.append(character_dict[key1[index]] + character_dict[sentence1[x]] - 25)
        else:
            difference.append(character_dict[key1[index]] + character_dict[sentence1[x]])

        index = index + 1
        cipher_sentence += character_dict_cipher[difference[x]]

    print("Cipher Text: " + cipher_sentence)
    cipher_to_plain(cipher_sentence, key)

# *************************************************************************************************************

# This function is passed cipher text and the key. First string is the cipher text and function ignores all
# non-alphabetic characters. All uppercase letters are converted to lower case. The second string is the key
# and can be 1 or more in length.


def cipher_to_plain(cipher_text, key):

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


def automate_decrypting_vigenere():
    # Prompt user for sentence to encrypt and the key.
    cipher_text = str(input("Enter a Cipher Text to decrypt: "))
    substring_text = str(input("Enter a substring found in Cipher Text: "))

    while True:
        key_size = int(input("Enter the max key size (1-10): "))

        if 1 <= key_size <= 10:
            break
        else:
            print("\nKey size does not match requirements. Please try again.\n")

    # Changes string to lowercase.
    cipher_text = cipher_text.lower()
    substring_text = substring_text.lower()

    # Regular expression that removes all upper case and non alphabetical characters.
    regular_expression = re.compile('[^a-za-z]')
    cipher_text = regular_expression.sub('', cipher_text)
    substring_text = regular_expression.sub('', substring_text)

# *************************************************************************************************************

print("Project 1: Vigenere Cipher\n")

while True:
    print("Select an option: ")
    print("1. Task One: Encryption then Decryption.")
    print("2. Task Two: Decrypting string with unknown key.")
    print("3. Quit Program.\n")

    answer = int(input("Option: "))
    print("")

    if answer == 1:
        plain_to_cipher()
        print("")
    elif answer == 2:
        automate_decrypting_vigenere()
        print("")
    elif answer == 3:
        break
    else:
        print("Incorrect option try again.\n")
