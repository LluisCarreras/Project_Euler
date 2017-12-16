# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:20:35 2016

@author: Lluís Carreras González

XOR decryption
Problem 59

Each character on a computer is assigned a unique code and the preferred 
standard is ASCII (American Standard Code for Information Interchange). For 
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to 
ASCII, then XOR each byte with a given value, taken from a secret key. The 
advantage with the XOR function is that using the same encryption key on the 
cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 
XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text 
message, and the key is made up of random bytes. The user would keep the 
encrypted message and the encryption key in different locations, and without 
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified 
method is to use a password as a key. If the password is shorter than the 
message, which is likely, the key is repeated cyclically throughout the 
message. The balance for this method is using a sufficiently long password 
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower 
case characters. Using cipher.txt (right click and 'Save Link/Target As...'), 
a file containing the encrypted ASCII codes, and the knowledge that the plain 
text must contain common English words, decrypt the message and find the sum 
of the ASCII values in the original text.
"""

import operator


def file_to_list(my_file):
    """
    Return a list with the int items in the given file.
    """
            
    return [int(x) for x in open(my_file, 'r').read().strip().split(",")]
    
    
def list_to_text(my_list):
    """
    Return a text converting the list of ASCII codes to characters.
    """
    
    return ''.join([chr(i) for i in my_list])
    
 
def decrypt(my_list, key):
    """
    Return the text obtained from decrypting the given list with the
    given key.
    """
    
    my_text = ''
    for idx in range(len(my_list)):
        decrypted_item = operator.xor(my_list[idx], key[idx % len(key)])
        my_text += chr(decrypted_item)
    return my_text
    
 
my_list = file_to_list('p059_cipher.txt') 
my_dict = {}  

for char1 in range(ord('a'), ord('z') + 1):
    for char2 in range(ord('a'), ord('z') + 1):
        for char3 in range(ord('a'), ord('z') + 1):
            key = [char1, char2, char3]
            key_str = ''.join([chr(c) for c in key])
            my_text = decrypt(my_list, key)
            my_words = my_text.split(" ")
            # Use the word "the" to check if the text obtained is an 
            # english text.
            if "the" in my_words:
                my_dict[key_str] = my_text
                
for k, v in my_dict.items():
    print(k)
    print(v)
    print()
            
for k, v in my_dict.items():
    original_text = v
 
total_sum = 0   
for letter in original_text:
    total_sum += ord(letter)
    
print(total_sum)