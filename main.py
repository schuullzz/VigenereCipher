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
    return cipher_to_plain(cipher_sentence, key)


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

    return plain_sentence


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

    key_indexes = list()
    index = 0
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True
    flag5 = True
    flag6 = True
    flag7 = True
    flag8 = True
    flag9 = True
    flag10 = True

    for x in range(key_size):
        key_indexes.append(0)

    while True:

        if index == key_size:
            print("Plain text not found.")
            break
        elif flag1:
            flag1 = False
            temp_flag = False
            passed_first_index = False
            possible_number_keys = 26 ** 1

            for z in range(possible_number_keys):
                possible_solution = cipher_to_plain(cipher_text, character_dict_cipher[key_indexes[0]])
                key_indexes[0] = key_indexes[0] + 1

                if key_indexes[0] % 26 == 0 and passed_first_index:
                    key_indexes[0] = 0

                passed_first_index = True

                if substring_text in possible_solution:
                    print("Key Found: " + character_dict_cipher[key_indexes[0] - 1])
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

            key_indexes[0] = 0

            if temp_flag:
                next_digit = input("Key size one finished would you like to continue? Enter yes or no: ")
                next_digit.lower()

                while True:
                    if next_digit == "yes":
                        continue
                    elif next_digit == "no":
                        break
                    else:
                        print("Wrong input. Try again.")

            index = index + 1
        elif flag2:
            flag2 = False
            temp_flag = False
            passed_first_index0 = False
            passed_first_index1 = False
            possible_number_keys = 26 ** 2

            for z in range(possible_number_keys):
                possible_key = character_dict_cipher[key_indexes[0]] + character_dict_cipher[key_indexes[1]]
                possible_solution = cipher_to_plain(cipher_text, possible_key)
                key_indexes[1] = key_indexes[1] + 1

                if key_indexes[1] % 26 == 0 and passed_first_index1:
                    key_indexes[0] = key_indexes[0] + 1
                    key_indexes[1] = 0
                    passed_first_index0 = True

                passed_first_index1 = True

                if key_indexes[0] % 26 == 0 and passed_first_index0:
                    key_indexes[1] = 0

                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

            key_indexes[0] = 0
            key_indexes[1] = 0

            if temp_flag:
                next_digit = input("Key size two finished would you like to continue? Enter yes or no: ")
                next_digit.lower()

                while True:
                    if next_digit == "yes":
                        continue
                    elif next_digit == "no":
                        break
                    else:
                        print("Wrong input. Try again.")

            index = index + 1
        elif flag3:
            flag3 = False
            temp_flag = False
            passed_first_index0 = False
            passed_first_index1 = False
            passed_first_index2 = False
            possible_number_keys = 26 ** 3

            for z in range(possible_number_keys):
                possible_key = character_dict_cipher[key_indexes[0]] + character_dict_cipher[key_indexes[1]] \
                               + character_dict_cipher[key_indexes[2]]
                possible_solution = cipher_to_plain(cipher_text, possible_key)
                key_indexes[2] = key_indexes[2] + 1

                if key_indexes[2] % 26 == 0 and passed_first_index2:
                    key_indexes[1] = key_indexes[1] + 1
                    key_indexes[2] = 0
                    passed_first_index1 = True

                passed_first_index2 = True

                if key_indexes[1] % 26 == 0 and passed_first_index1:
                    key_indexes[0] = key_indexes[0] + 1
                    key_indexes[1] = 0
                    passed_first_index1 = False
                    passed_first_index0 = True

                if key_indexes[0] % 26 == 0 and passed_first_index0:
                    key_indexes[0] = 0

                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0

            if temp_flag:
                next_digit = input("Key size three finished would you like to continue? Enter yes or no: ")
                next_digit.lower()

                while True:
                    if next_digit == "yes":
                        continue
                    elif next_digit == "no":
                        break
                    else:
                        print("Wrong input. Try again.")

            index = index + 1
        elif flag4:
            flag4 = False
            temp_flag = False
            passed_first_index0 = False
            passed_first_index1 = False
            passed_first_index2 = False
            passed_first_index3 = False
            possible_number_keys = 26 ** 4

            for z in range(possible_number_keys):
                possible_key = character_dict_cipher[key_indexes[0]] + character_dict_cipher[key_indexes[1]] \
                               + character_dict_cipher[key_indexes[2]] + character_dict_cipher[key_indexes[3]]
                possible_solution = cipher_to_plain(cipher_text, possible_key)
                key_indexes[3] = key_indexes[3] + 1

                if key_indexes[3] % 26 == 0 and passed_first_index3:
                    key_indexes[2] = key_indexes[2] + 1
                    key_indexes[3] = 0
                    passed_first_index2 = True

                passed_first_index3 = True

                if key_indexes[2] % 26 == 0 and passed_first_index2:
                    key_indexes[1] = key_indexes[1] + 1
                    key_indexes[2] = 0
                    passed_first_index2 = False
                    passed_first_index1 = True

                if key_indexes[1] % 26 == 0 and passed_first_index1:
                    key_indexes[0] = key_indexes[0] + 1
                    key_indexes[1] = 0
                    passed_first_index1 = False
                    passed_first_index0 = True

                if key_indexes[0] % 26 == 0 and passed_first_index0:
                    key_indexes[0] = 0

                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0

            if temp_flag:
                next_digit = input("Key size four finished would you like to continue? Enter yes or no: ")
                next_digit.lower()

                while True:
                    if next_digit == "yes":
                        continue
                    elif next_digit == "no":
                        break
                    else:
                        print("Wrong input. Try again.")

            index = index + 1
        elif flag5:
            flag5 = False
            temp_flag = False
            passed_first_index0 = False
            passed_first_index1 = False
            passed_first_index2 = False
            passed_first_index3 = False
            passed_first_index4 = False
            possible_number_keys = 26 ** 5

            for z in range(possible_number_keys):
                possible_key = character_dict_cipher[key_indexes[0]] + character_dict_cipher[key_indexes[1]] \
                               + character_dict_cipher[key_indexes[2]] + character_dict_cipher[key_indexes[3]] \
                               + character_dict_cipher[key_indexes[4]]
                possible_solution = cipher_to_plain(cipher_text, possible_key)
                key_indexes[4] = key_indexes[4] + 1

                if key_indexes[4] % 26 == 0 and passed_first_index4:
                    key_indexes[3] = key_indexes[3] + 1
                    key_indexes[4] = 0
                    passed_first_index3 = True

                passed_first_index4 = True

                if key_indexes[3] % 26 == 0 and passed_first_index3:
                    key_indexes[2] = key_indexes[2] + 1
                    key_indexes[3] = 0
                    passed_first_index3 = False
                    passed_first_index2 = True

                if key_indexes[2] % 26 == 0 and passed_first_index2:
                    key_indexes[1] = key_indexes[1] + 1
                    key_indexes[2] = 0
                    passed_first_index2 = False
                    passed_first_index1 = True

                if key_indexes[1] % 26 == 0 and passed_first_index1:
                    key_indexes[0] = key_indexes[0] + 1
                    key_indexes[1] = 0
                    passed_first_index1 = False
                    passed_first_index0 = True

                if key_indexes[0] % 26 == 0 and passed_first_index0:
                    key_indexes[0] = 0

                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0
            key_indexes[4] = 0

            if temp_flag:
                next_digit = input("Key size five finished would you like to continue? Enter yes or no: ")
                next_digit.lower()

                while True:
                    if next_digit == "yes":
                        continue
                    elif next_digit == "no":
                        break
                    else:
                        print("Wrong input. Try again.")

            index = index + 1
        elif flag6:
            flag6 = False
            temp_flag = False
            passed_first_index0 = False
            passed_first_index1 = False
            passed_first_index2 = False
            passed_first_index3 = False
            passed_first_index4 = False
            passed_first_index5 = False
            possible_number_keys = 26 ** 6

            for z in range(possible_number_keys):
                possible_key = character_dict_cipher[key_indexes[0]] + character_dict_cipher[key_indexes[1]] \
                               + character_dict_cipher[key_indexes[2]] + character_dict_cipher[key_indexes[3]] \
                               + character_dict_cipher[key_indexes[4]] + character_dict_cipher[key_indexes[5]]
                possible_solution = cipher_to_plain(cipher_text, possible_key)
                key_indexes[5] = key_indexes[5] + 1

                if key_indexes[5] % 26 == 0 and passed_first_index5:
                    key_indexes[4] = key_indexes[4] + 1
                    key_indexes[5] = 0
                    passed_first_index4 = True

                passed_first_index5 = True

                if key_indexes[4] % 26 == 0 and passed_first_index4:
                    key_indexes[3] = key_indexes[3] + 1
                    key_indexes[4] = 0
                    passed_first_index4 = False
                    passed_first_index3 = True

                if key_indexes[3] % 26 == 0 and passed_first_index3:
                    key_indexes[2] = key_indexes[2] + 1
                    key_indexes[3] = 0
                    passed_first_index3 = False
                    passed_first_index2 = True

                if key_indexes[2] % 26 == 0 and passed_first_index2:
                    key_indexes[1] = key_indexes[1] + 1
                    key_indexes[2] = 0
                    passed_first_index2 = False
                    passed_first_index1 = True

                if key_indexes[1] % 26 == 0 and passed_first_index1:
                    key_indexes[0] = key_indexes[0] + 1
                    key_indexes[1] = 0
                    passed_first_index1 = False
                    passed_first_index0 = True

                if key_indexes[0] % 26 == 0 and passed_first_index0:
                    key_indexes[0] = 0

                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0
            key_indexes[4] = 0
            key_indexes[5] = 0

            if temp_flag:
                next_digit = input("Key size six finished would you like to continue? Enter yes or no: ")
                next_digit.lower()

                while True:
                    if next_digit == "yes":
                        continue
                    elif next_digit == "no":
                        break
                    else:
                        print("Wrong input. Try again.")

            index = index + 1
        elif flag7:
            flag7 = False
            temp_flag = False
            passed_first_index0 = False
            passed_first_index1 = False
            passed_first_index2 = False
            passed_first_index3 = False
            passed_first_index4 = False
            passed_first_index5 = False
            passed_first_index6 = False
            possible_number_keys = 26 ** 7

            for z in range(possible_number_keys):
                possible_key = character_dict_cipher[key_indexes[0]] + character_dict_cipher[key_indexes[1]] \
                               + character_dict_cipher[key_indexes[2]] + character_dict_cipher[key_indexes[3]] \
                               + character_dict_cipher[key_indexes[4]] + character_dict_cipher[key_indexes[5]] \
                               + character_dict_cipher[key_indexes[6]]
                possible_solution = cipher_to_plain(cipher_text, possible_key)
                key_indexes[6] = key_indexes[6] + 1

                if key_indexes[6] % 26 == 0 and passed_first_index6:
                    key_indexes[5] = key_indexes[5] + 1
                    key_indexes[6] = 0
                    passed_first_index5 = True

                passed_first_index6 = True

                if key_indexes[5] % 26 == 0 and passed_first_index5:
                    key_indexes[4] = key_indexes[4] + 1
                    key_indexes[5] = 0
                    passed_first_index5 = False
                    passed_first_index4 = True

                if key_indexes[4] % 26 == 0 and passed_first_index4:
                    key_indexes[3] = key_indexes[3] + 1
                    key_indexes[4] = 0
                    passed_first_index4 = False
                    passed_first_index3 = True

                if key_indexes[3] % 26 == 0 and passed_first_index3:
                    key_indexes[2] = key_indexes[2] + 1
                    key_indexes[3] = 0
                    passed_first_index3 = False
                    passed_first_index2 = True

                if key_indexes[2] % 26 == 0 and passed_first_index2:
                    key_indexes[1] = key_indexes[1] + 1
                    key_indexes[2] = 0
                    passed_first_index2 = False
                    passed_first_index1 = True

                if key_indexes[1] % 26 == 0 and passed_first_index1:
                    key_indexes[0] = key_indexes[0] + 1
                    key_indexes[1] = 0
                    passed_first_index1 = False
                    passed_first_index0 = True

                if key_indexes[0] % 26 == 0 and passed_first_index0:
                    key_indexes[0] = 0

                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0
            key_indexes[4] = 0
            key_indexes[5] = 0
            key_indexes[6] = 0

            if temp_flag:
                next_digit = input("Key size seven finished would you like to continue? Enter yes or no: ")
                next_digit.lower()

                while True:
                    if next_digit == "yes":
                        continue
                    elif next_digit == "no":
                        break
                    else:
                        print("Wrong input. Try again.")

            index = index + 1
        elif flag8:
            flag8 = False
            temp_flag = False
            passed_first_index0 = False
            passed_first_index1 = False
            passed_first_index2 = False
            passed_first_index3 = False
            passed_first_index4 = False
            passed_first_index5 = False
            passed_first_index6 = False
            passed_first_index7 = False
            possible_number_keys = 26 ** 8

            for z in range(possible_number_keys):
                possible_key = character_dict_cipher[key_indexes[0]] + character_dict_cipher[key_indexes[1]] \
                               + character_dict_cipher[key_indexes[2]] + character_dict_cipher[key_indexes[3]] \
                               + character_dict_cipher[key_indexes[4]] + character_dict_cipher[key_indexes[5]] \
                               + character_dict_cipher[key_indexes[6]] + character_dict_cipher[key_indexes[7]]
                print(possible_key)
                possible_solution = cipher_to_plain(cipher_text, possible_key)
                key_indexes[7] = key_indexes[7] + 1

                if key_indexes[7] % 26 == 0 and passed_first_index7:
                    key_indexes[6] = key_indexes[6] + 1
                    key_indexes[7] = 0
                    passed_first_index6 = True

                passed_first_index7 = True

                if key_indexes[6] % 26 == 0 and passed_first_index6:
                    key_indexes[5] = key_indexes[5] + 1
                    key_indexes[6] = 0
                    passed_first_index6 = False
                    passed_first_index5 = True

                if key_indexes[5] % 26 == 0 and passed_first_index5:
                    key_indexes[4] = key_indexes[4] + 1
                    key_indexes[5] = 0
                    passed_first_index5 = False
                    passed_first_index4 = True

                if key_indexes[4] % 26 == 0 and passed_first_index4:
                    key_indexes[3] = key_indexes[3] + 1
                    key_indexes[4] = 0
                    passed_first_index4 = False
                    passed_first_index3 = True

                if key_indexes[3] % 26 == 0 and passed_first_index3:
                    key_indexes[2] = key_indexes[2] + 1
                    key_indexes[3] = 0
                    passed_first_index3 = False
                    passed_first_index2 = True

                if key_indexes[2] % 26 == 0 and passed_first_index2:
                    key_indexes[1] = key_indexes[1] + 1
                    key_indexes[2] = 0
                    passed_first_index2 = False
                    passed_first_index1 = True

                if key_indexes[1] % 26 == 0 and passed_first_index1:
                    key_indexes[0] = key_indexes[0] + 1
                    key_indexes[1] = 0
                    passed_first_index1 = False
                    passed_first_index0 = True

                if key_indexes[0] % 26 == 0 and passed_first_index0:
                    key_indexes[0] = 0

                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0
            key_indexes[4] = 0
            key_indexes[5] = 0
            key_indexes[6] = 0
            key_indexes[7] = 0

            if temp_flag:
                next_digit = input("Key size eight finished would you like to continue? Enter yes or no: ")
                next_digit.lower()

                while True:
                    if next_digit == "yes":
                        continue
                    elif next_digit == "no":
                        break
                    else:
                        print("Wrong input. Try again.")

            index = index + 1
        elif flag9:
            flag9 = False
            temp_flag = False
            passed_first_index0 = False
            passed_first_index1 = False
            passed_first_index2 = False
            passed_first_index3 = False
            passed_first_index4 = False
            passed_first_index5 = False
            passed_first_index6 = False
            passed_first_index7 = False
            passed_first_index8 = False
            possible_number_keys = 26 ** 9

            for z in range(possible_number_keys):
                possible_key = character_dict_cipher[key_indexes[0]] + character_dict_cipher[key_indexes[1]] \
                               + character_dict_cipher[key_indexes[2]] + character_dict_cipher[key_indexes[3]] \
                               + character_dict_cipher[key_indexes[4]] + character_dict_cipher[key_indexes[5]] \
                               + character_dict_cipher[key_indexes[6]] + character_dict_cipher[key_indexes[7]] \
                               + character_dict_cipher[key_indexes[8]]
                possible_solution = cipher_to_plain(cipher_text, possible_key)
                key_indexes[8] = key_indexes[8] + 1

                if key_indexes[8] % 26 == 0 and passed_first_index8:
                    key_indexes[7] = key_indexes[7] + 1
                    key_indexes[8] = 0
                    passed_first_index7 = True

                passed_first_index8 = True

                if key_indexes[7] % 26 == 0 and passed_first_index7:
                    key_indexes[6] = key_indexes[6] + 1
                    key_indexes[7] = 0
                    passed_first_index7 = False
                    passed_first_index6 = True

                if key_indexes[6] % 26 == 0 and passed_first_index6:
                    key_indexes[5] = key_indexes[5] + 1
                    key_indexes[6] = 0
                    passed_first_index6 = False
                    passed_first_index5 = True

                if key_indexes[5] % 26 == 0 and passed_first_index5:
                    key_indexes[4] = key_indexes[4] + 1
                    key_indexes[5] = 0
                    passed_first_index5 = False
                    passed_first_index4 = True

                if key_indexes[4] % 26 == 0 and passed_first_index4:
                    key_indexes[3] = key_indexes[3] + 1
                    key_indexes[4] = 0
                    passed_first_index4 = False
                    passed_first_index3 = True

                if key_indexes[3] % 26 == 0 and passed_first_index3:
                    key_indexes[2] = key_indexes[2] + 1
                    key_indexes[3] = 0
                    passed_first_index3 = False
                    passed_first_index2 = True

                if key_indexes[2] % 26 == 0 and passed_first_index2:
                    key_indexes[1] = key_indexes[1] + 1
                    key_indexes[2] = 0
                    passed_first_index2 = False
                    passed_first_index1 = True

                if key_indexes[1] % 26 == 0 and passed_first_index1:
                    key_indexes[0] = key_indexes[0] + 1
                    key_indexes[1] = 0
                    passed_first_index1 = False
                    passed_first_index0 = True

                if key_indexes[0] % 26 == 0 and passed_first_index0:
                    key_indexes[0] = 0

                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0
            key_indexes[4] = 0
            key_indexes[5] = 0
            key_indexes[6] = 0
            key_indexes[7] = 0
            key_indexes[8] = 0

            if temp_flag:
                next_digit = input("Key size nine finished would you like to continue? Enter yes or no: ")
                next_digit.lower()

                while True:
                    if next_digit == "yes":
                        continue
                    elif next_digit == "no":
                        break
                    else:
                        print("Wrong input. Try again.")

            index = index + 1
        elif flag10:
            flag10 = False
            temp_flag = False
            passed_first_index0 = False
            passed_first_index1 = False
            passed_first_index2 = False
            passed_first_index3 = False
            passed_first_index4 = False
            passed_first_index5 = False
            passed_first_index6 = False
            passed_first_index7 = False
            passed_first_index8 = False
            passed_first_index9 = False
            possible_number_keys = 26 ** 10

            for z in range(possible_number_keys):
                possible_key = character_dict_cipher[key_indexes[0]] + character_dict_cipher[key_indexes[1]] \
                               + character_dict_cipher[key_indexes[2]] + character_dict_cipher[key_indexes[3]] \
                               + character_dict_cipher[key_indexes[4]] + character_dict_cipher[key_indexes[5]] \
                               + character_dict_cipher[key_indexes[6]] + character_dict_cipher[key_indexes[7]] \
                               + character_dict_cipher[key_indexes[8]] + character_dict_cipher[key_indexes[9]]
                possible_solution = cipher_to_plain(cipher_text, possible_key)
                key_indexes[9] = key_indexes[9] + 1

                if key_indexes[9] % 26 == 0 and passed_first_index9:
                    key_indexes[8] = key_indexes[8] + 1
                    key_indexes[9] = 0
                    passed_first_index8 = True

                passed_first_index9 = True

                if key_indexes[8] % 26 == 0 and passed_first_index8:
                    key_indexes[7] = key_indexes[7] + 1
                    key_indexes[8] = 0
                    passed_first_index8 = False
                    passed_first_index7 = True

                if key_indexes[7] % 26 == 0 and passed_first_index7:
                    key_indexes[6] = key_indexes[6] + 1
                    key_indexes[7] = 0
                    passed_first_index7 = False
                    passed_first_index6 = True

                if key_indexes[6] % 26 == 0 and passed_first_index6:
                    key_indexes[5] = key_indexes[5] + 1
                    key_indexes[6] = 0
                    passed_first_index6 = False
                    passed_first_index5 = True

                if key_indexes[5] % 26 == 0 and passed_first_index5:
                    key_indexes[4] = key_indexes[4] + 1
                    key_indexes[5] = 0
                    passed_first_index5 = False
                    passed_first_index4 = True

                if key_indexes[4] % 26 == 0 and passed_first_index4:
                    key_indexes[3] = key_indexes[3] + 1
                    key_indexes[4] = 0
                    passed_first_index4 = False
                    passed_first_index3 = True

                if key_indexes[3] % 26 == 0 and passed_first_index3:
                    key_indexes[2] = key_indexes[2] + 1
                    key_indexes[3] = 0
                    passed_first_index3 = False
                    passed_first_index2 = True

                if key_indexes[2] % 26 == 0 and passed_first_index2:
                    key_indexes[1] = key_indexes[1] + 1
                    key_indexes[2] = 0
                    passed_first_index2 = False
                    passed_first_index1 = True

                if key_indexes[1] % 26 == 0 and passed_first_index1:
                    key_indexes[0] = key_indexes[0] + 1
                    key_indexes[1] = 0
                    passed_first_index1 = False
                    passed_first_index0 = True

                if key_indexes[0] % 26 == 0 and passed_first_index0:
                    key_indexes[0] = 0

                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0
            key_indexes[4] = 0
            key_indexes[5] = 0
            key_indexes[6] = 0
            key_indexes[7] = 0
            key_indexes[8] = 0
            key_indexes[9] = 0

            if temp_flag:
                next_digit = input("Key size ten finished would you like to continue? Enter yes or no: ")
                next_digit.lower()

                while True:
                    if next_digit == "yes":
                        continue
                    elif next_digit == "no":
                        break
                    else:
                        print("Wrong input. Try again.")

            index = index + 1


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
        print("Plain Text: " + plain_to_cipher() + "\n")
    elif answer == 2:
        automate_decrypting_vigenere()
        print("")
    elif answer == 3:
        break
    else:
        print("Incorrect option try again.\n")
