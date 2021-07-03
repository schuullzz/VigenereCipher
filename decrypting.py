import cipher
import re

# Prompts user for ciphertext, a known word found in the plaintext, and the max size of
# the key. Then through a brute-force algorithm searches the possible keys to find the
# known word found in the plaintext. If a match is found the user is prompted to continue
# or end search. At the end of each key length the user is asked if they desire to end search.

# If key is longer than six digits long this method will take a long time to complete.
# Each key length will follow 26 ^ n where n is the number of digits. So efficiency will
# be constant but the larger the number the more impractical it is to find the right key.
# (26 ^ n where n is 7, 8, 9, or 10 will take far too long to complete).


def automate_decrypting_vigenere():
    # Prompt user for sentence to encrypt and the key.
    cipher_text = str(input("Enter a Cipher Text to decrypt: "))
    substring_text = str(input("Enter a substring found in Cipher Text: "))

    # Request user to enter in a number between 1-10
    while True:
        key_size = int(input("Enter the max key size (1-10): "))

        if 1 <= key_size <= 10:
            break
        else:
            print("\nKey size does not match requirements. Please try again.")

    print("")

    # Changes string to lowercase.
    cipher_text = cipher_text.lower()
    substring_text = substring_text.lower()

    # Regular expression that removes all upper case and non alphabetical characters.
    regular_expression = re.compile('[^a-za-z]')
    cipher_text = regular_expression.sub('', cipher_text)
    substring_text = regular_expression.sub('', substring_text)

    # Creates a key list
    key_indexes = list()
    # keeps track of the current index
    index = 0
    # All flags are set to true for a max of key length 10
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

    # Sets all indexes to zero
    for x in range(key_size):
        key_indexes.append(0)

    # continuous loop that breaks when no key is found or when user is done.
    while True:

        # series of ifs that determine how many digits are being checked.
        if index == key_size:
            print("Plain text not found.")
            break
        elif flag1:
            flag1 = False
            temp_flag = False
            passed_first_index = False
            possible_number_keys = 26 ** 1

            # for loop that checks desired number of digits for the correct key.
            for z in range(possible_number_keys):
                possible_solution = cipher.cipher_to_plain(cipher_text, cipher.character_dict_cipher[key_indexes[0]])
                key_indexes[0] = key_indexes[0] + 1

                if key_indexes[0] % 26 == 0 and passed_first_index:
                    key_indexes[0] = 0

                passed_first_index = True

                # if substring is found then key and plaintext is displayed. User will be asked
                # if they desire to continue searching.
                if substring_text in possible_solution:
                    print("Key Found: " + cipher.character_dict_cipher[key_indexes[0] - 1])
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()
                        print("")

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

                    if temp_flag:
                        break

            key_indexes[0] = 0

            if temp_flag:
                break

            # Prompts user if they would like to move on to next key length.
            while True:
                next_digit = input("Key size one finished would you like to continue? Enter yes or no: ")
                next_digit.lower()
                print("")

                if next_digit == "yes":
                    break
                elif next_digit == "no":
                    return
                else:
                    print("Wrong input. Try again.")

            index = index + 1
        elif flag2:
            flag2 = False
            temp_flag = False
            passed_first_index0 = False
            passed_first_index1 = False
            possible_number_keys = 26 ** 2

            # for loop that checks desired number of digits for the correct key.
            for z in range(possible_number_keys):
                possible_key = cipher.character_dict_cipher[key_indexes[0]] + cipher.character_dict_cipher[key_indexes[1]]
                possible_solution = cipher.cipher_to_plain(cipher_text, possible_key)
                key_indexes[1] = key_indexes[1] + 1

                if key_indexes[1] % 26 == 0 and passed_first_index1:
                    key_indexes[0] = key_indexes[0] + 1
                    key_indexes[1] = 0
                    passed_first_index0 = True

                passed_first_index1 = True

                if key_indexes[0] % 26 == 0 and passed_first_index0:
                    key_indexes[1] = 0

                # if substring is found then key and plaintext is displayed. User will be asked
                # if they desire to continue searching.
                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()
                        print("")

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")
                    if temp_flag:
                        break

            key_indexes[0] = 0
            key_indexes[1] = 0

            if temp_flag:
                break

            # Prompts user if they would like to move on to next key length.
            while True:
                next_digit = input("Key size two finished would you like to continue? Enter yes or no: ")
                next_digit.lower()
                print("")

                if next_digit == "yes":
                    break
                elif next_digit == "no":
                    return
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

            # for loop that checks desired number of digits for the correct key.
            for z in range(possible_number_keys):
                possible_key = cipher.character_dict_cipher[key_indexes[0]] + cipher.character_dict_cipher[key_indexes[1]] \
                               + cipher.character_dict_cipher[key_indexes[2]]
                possible_solution = cipher.cipher_to_plain(cipher_text, possible_key)
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

                # if substring is found then key and plaintext is displayed. User will be asked
                # if they desire to continue searching.
                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()
                        print("")

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

                    if temp_flag:
                        break

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0

            if temp_flag:
                break

            # Prompts user if they would like to move on to next key length.
            while True:
                next_digit = input("Key size three finished would you like to continue? Enter yes or no: ")
                next_digit.lower()
                print("")

                if next_digit == "yes":
                    break
                elif next_digit == "no":
                    return
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

            # for loop that checks desired number of digits for the correct key.
            for z in range(possible_number_keys):
                possible_key = cipher.character_dict_cipher[key_indexes[0]] + cipher.character_dict_cipher[key_indexes[1]] \
                               + cipher.character_dict_cipher[key_indexes[2]] + cipher.character_dict_cipher[key_indexes[3]]
                possible_solution = cipher.cipher_to_plain(cipher_text, possible_key)
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

                # if substring is found then key and plaintext is displayed. User will be asked
                # if they desire to continue searching.
                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()
                        print("")

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

                    if temp_flag:
                        break

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0

            if temp_flag:
                break

            # Prompts user if they would like to move on to next key length.
            while True:
                next_digit = input("Key size four finished would you like to continue? Enter yes or no: ")
                next_digit.lower()
                print("")

                if next_digit == "yes":
                    break
                elif next_digit == "no":
                    return
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

            # for loop that checks desired number of digits for the correct key.
            for z in range(possible_number_keys):
                possible_key = cipher.character_dict_cipher[key_indexes[0]] + cipher.character_dict_cipher[key_indexes[1]] \
                               + cipher.character_dict_cipher[key_indexes[2]] + cipher.character_dict_cipher[key_indexes[3]] \
                               + cipher.character_dict_cipher[key_indexes[4]]
                possible_solution = cipher.cipher_to_plain(cipher_text, possible_key)
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

                # if substring is found then key and plaintext is displayed. User will be asked
                # if they desire to continue searching.
                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()
                        print("")

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

                    if temp_flag:
                        break

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0
            key_indexes[4] = 0

            if temp_flag:
                break

            # Prompts user if they would like to move on to next key length.
            while True:
                next_digit = input("Key size five finished would you like to continue? Enter yes or no: ")
                next_digit.lower()
                print("")

                if next_digit == "yes":
                    break
                elif next_digit == "no":
                    return
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

            # for loop that checks desired number of digits for the correct key.
            for z in range(possible_number_keys):
                possible_key = cipher.character_dict_cipher[key_indexes[0]] + cipher.character_dict_cipher[key_indexes[1]] \
                               + cipher.character_dict_cipher[key_indexes[2]] + cipher.character_dict_cipher[key_indexes[3]] \
                               + cipher.character_dict_cipher[key_indexes[4]] + cipher.character_dict_cipher[key_indexes[5]]
                possible_solution = cipher.cipher_to_plain(cipher_text, possible_key)
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

                # if substring is found then key and plaintext is displayed. User will be asked
                # if they desire to continue searching.
                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()
                        print("")

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

                    if temp_flag:
                        break

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0
            key_indexes[4] = 0
            key_indexes[5] = 0

            if temp_flag:
                break

            # Prompts user if they would like to move on to next key length.
            while True:
                next_digit = input("Key size six finished would you like to continue? Enter yes or no: ")
                next_digit.lower()
                print("")

                if next_digit == "yes":
                    break
                elif next_digit == "no":
                    return
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

            # for loop that checks desired number of digits for the correct key.
            for z in range(possible_number_keys):
                possible_key = cipher.character_dict_cipher[key_indexes[0]] + cipher.character_dict_cipher[key_indexes[1]] \
                               + cipher.character_dict_cipher[key_indexes[2]] + cipher.character_dict_cipher[key_indexes[3]] \
                               + cipher.character_dict_cipher[key_indexes[4]] + cipher.character_dict_cipher[key_indexes[5]] \
                               + cipher.character_dict_cipher[key_indexes[6]]
                possible_solution = cipher.cipher_to_plain(cipher_text, possible_key)
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

                # if substring is found then key and plaintext is displayed. User will be asked
                # if they desire to continue searching.
                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()
                        print("")

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

                    if temp_flag:
                        break

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0
            key_indexes[4] = 0
            key_indexes[5] = 0
            key_indexes[6] = 0

            if temp_flag:
                break

            # Prompts user if they would like to move on to next key length.
            while True:
                next_digit = input("Key size seven finished would you like to continue? Enter yes or no: ")
                next_digit.lower()
                print("")

                if next_digit == "yes":
                    break
                elif next_digit == "no":
                    return
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

            # for loop that checks desired number of digits for the correct key.
            for z in range(possible_number_keys):
                possible_key = cipher.character_dict_cipher[key_indexes[0]] + cipher.character_dict_cipher[key_indexes[1]] \
                               + cipher.character_dict_cipher[key_indexes[2]] + cipher.character_dict_cipher[key_indexes[3]] \
                               + cipher.character_dict_cipher[key_indexes[4]] + cipher.character_dict_cipher[key_indexes[5]] \
                               + cipher.character_dict_cipher[key_indexes[6]] + cipher.character_dict_cipher[key_indexes[7]]
                print(possible_key)
                possible_solution = cipher.cipher_to_plain(cipher_text, possible_key)
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

                # if substring is found then key and plaintext is displayed. User will be asked
                # if they desire to continue searching.
                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()
                        print("")

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

                    if temp_flag:
                        break

            key_indexes[0] = 0
            key_indexes[1] = 0
            key_indexes[2] = 0
            key_indexes[3] = 0
            key_indexes[4] = 0
            key_indexes[5] = 0
            key_indexes[6] = 0
            key_indexes[7] = 0

            if temp_flag:
                break

            # Prompts user if they would like to move on to next key length.
            while True:
                next_digit = input("Key size eight finished would you like to continue? Enter yes or no: ")
                next_digit.lower()
                print("")

                if next_digit == "yes":
                    break
                elif next_digit == "no":
                    return
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

            # for loop that checks desired number of digits for the correct key.
            for z in range(possible_number_keys):
                possible_key = cipher.character_dict_cipher[key_indexes[0]] + cipher.character_dict_cipher[key_indexes[1]] \
                               + cipher.character_dict_cipher[key_indexes[2]] + cipher.character_dict_cipher[key_indexes[3]] \
                               + cipher.character_dict_cipher[key_indexes[4]] + cipher.character_dict_cipher[key_indexes[5]] \
                               + cipher.character_dict_cipher[key_indexes[6]] + cipher.character_dict_cipher[key_indexes[7]] \
                               + cipher.character_dict_cipher[key_indexes[8]]
                possible_solution = cipher.cipher_to_plain(cipher_text, possible_key)
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

                # if substring is found then key and plaintext is displayed. User will be asked
                # if they desire to continue searching.
                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()
                        print("")

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

                    if temp_flag:
                        break

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
                break

            # Prompts user if they would like to move on to next key length.
            while True:
                next_digit = input("Key size nine finished would you like to continue? Enter yes or no: ")
                next_digit.lower()
                print("")

                if next_digit == "yes":
                    break
                elif next_digit == "no":
                    continue
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

            # for loop that checks desired number of digits for the correct key.
            for z in range(possible_number_keys):
                possible_key = cipher.character_dict_cipher[key_indexes[0]] + cipher.character_dict_cipher[key_indexes[1]] \
                               + cipher.character_dict_cipher[key_indexes[2]] + cipher.character_dict_cipher[key_indexes[3]] \
                               + cipher.character_dict_cipher[key_indexes[4]] + cipher.character_dict_cipher[key_indexes[5]] \
                               + cipher.character_dict_cipher[key_indexes[6]] + cipher.character_dict_cipher[key_indexes[7]] \
                               + cipher.character_dict_cipher[key_indexes[8]] + cipher.character_dict_cipher[key_indexes[9]]
                possible_solution = cipher.cipher_to_plain(cipher_text, possible_key)
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

                # if substring is found then key and plaintext is displayed. User will be asked
                # if they desire to continue searching.
                if substring_text in possible_solution:
                    print("Key Found: " + possible_key)
                    print("Plain Text Found: " + possible_solution)

                    while True:
                        continue_program = input("Would you like to continue? Enter yes or no: ")
                        continue_program.lower()
                        print("")

                        if continue_program == "yes":
                            temp_flag = False
                            break
                        elif continue_program == "no":
                            temp_flag = True
                            break
                        else:
                            print("Wrong input. Try again.")

                    if temp_flag:
                        break

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
                break

            # Prompts user if they would like to move on to next key length.
            while True:
                next_digit = input("Key size ten2 finished would you like to continue? Enter yes or no: ")
                next_digit.lower()
                print("")

                if next_digit == "yes":
                    break
                elif next_digit == "no":
                    return
                else:
                    print("Wrong input. Try again.")

            index = index + 1
