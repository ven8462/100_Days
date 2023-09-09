#!/usr/bin/python3

from sys import exit
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(message, shift_no, cipher_direction):
    """combining the encrypt and decrypt function in one function"""
    cipher_text = ""
    if cipher_direction == "decode":
        shift_no *= -1
    for chars in message:
        if chars in alphabet:
            position = alphabet.index(chars)
            new_position = position + shift_no
            new_chars = alphabet[new_position]
            cipher_text += new_chars
        else:
            cipher_text += chars
    print(f"the {direction}d message is {cipher_text}") 





while True:
    prompt = ['encode', 'decode']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction not in prompt:
        direction = input('Please enter the right keyword❗, type in "encode" to encrypt or type in "decode" to decrypt\n')
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    

    shift = shift % 52
    cipher(shift_no=shift,message=text,cipher_direction=direction)


    rerun = input("\nHey!, Do you wish to rerun the program😊?: ").lower()
    if rerun == "no":
        print("Thank you for using the Caesar Cipher program by Lavender❤️, Bye Bye😍😍")
        exit(0)







# def encrypt(plain_text, shift):
#     encoded_text = ""
#     for letters in plain_text:
#         position = alphabet.index(letters)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         encoded_text += new_letter

#     print("the encrypted text is",encoded_text)



# def decrypt(plain_text, shift):
#     decoded_text = ""
#     for letters in plain_text:
#         position = alphabet.index(letters)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         decoded_text += new_letter
#     print("the decrypted code is", decoded_text)


# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("please enter encode or decode")
