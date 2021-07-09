# VigenereCipher
## main.py cipher.py decrypting.py

## Description
```
This project involves a substitution cipher, encrytion, decryption,
and using a brute-force algorithm to find an unknown key. 
```

## Tasks
```
1. Write a function that will take in two strings and encrypt the first 
string with the second string using the Vigenere ciphere. The first string 
is the plaintext and your function should ignore all non-alphabetic characters 
(or your code can remove them from the string). All uppercase letters should 
be treated as lowercase letters (or you can convert the string to all lowercase letters). 
The second string is the key and it should be able to be from 1 character long to even 
longer than the plaintext string itself.Then write a function that, given two strings, 
decrypts the first string using the second string. Same conditions should apply as before.
Once these functions are completed, have your main body prompt the user for a string to 
encode, then a key string, then perform the encryption of the plaintext and output the 
ciphertest.Then decrypt it and show the resulting plaintext.

2. In this task, we are wanting to automate the process of decrypting a string using the 
vignere ciphere. In the main body, prompt the user for a ciphertext string encoded by the 
vignere cipher with an unknown key. Then prompt the user for a substring that we know has 
to be in the plaintext and a maximum size of the key (from 1 to 10 let us say). Your code 
should then brute-force the vignere cipher by decrypting the text using a possible key and 
then examining the possible plaintext for the substring. If the substring is in the possible 
plaintext, your code should print it out as a possible result, along with the key found, and 
then prompt the user if they would like to continue. You should also stop at every increment 
of keysize and ask them if they wish to continue the brute force.
```

## Usage
```
PyCharm Edu 2021.1.1

Project 1: Vigenere Cipher

Select an option:
1. Task One: Encryption then Decryption.
2. Task Two: Decrypting string with unknown key.
3. Quit Program
```


