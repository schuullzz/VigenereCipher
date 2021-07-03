# Timothy Schultz
# Professor Hauschild
# CS 4762 Introduction to Cryptography
# for Computer Security
# Project 1
# 6/25/2021

import cipher
import decrypting

# *************************************************************************************************************

print("Project 1: Vigenere Cipher\n")

# While statement acting a switch statement for possible option for user.
while True:
    print("Select an option: ")
    print("1. Task One: Encryption then Decryption.")
    print("2. Task Two: Decrypting string with unknown key.")
    print("3. Quit Program.\n")

    answer = int(input("Option: "))
    print("")

    if answer == 1:
        print("Plain Text: " + cipher.plain_to_cipher() + "\n")
    elif answer == 2:
        decrypting.automate_decrypting_vigenere()
        print("")
    elif answer == 3:
        break
    else:
        print("Incorrect option try again.\n")
