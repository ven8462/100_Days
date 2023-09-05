#!/usr/bin/python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(plain_text, shift):
    encoded_text = ""
    for letters in plain_text:
        position = alphabet.index(letters)
        new_position = position + shift
        new_letter = alphabet[new_position]
        encoded_text += new_letter

    print("the encrypted text is",encoded_text)



def decrypt(plain_text, shift):
    decoded_text = ""
    for letters in plain_text:
        position = alphabet.index(letters)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decoded_text += new_letter
    print("the decrypted code is", decoded_text)


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("please enter encode or decode")
