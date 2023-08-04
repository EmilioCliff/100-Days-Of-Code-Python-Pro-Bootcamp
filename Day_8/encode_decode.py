#!/usr/bin/python3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(plain_text, no_of_shift):
  encrypt_text = ""
  for letter in plain_text:
    if letter == " ":
      continue
    position = alphabet.index(letter)
    new_position = position+no_of_shift
    if new_position > len(alphabet) - 1:
      new_position -= len(alphabet)
    encrypt_text+=alphabet[new_position]
  print(encrypt_text)
  
def decrypt(encrypt_text, no_of_shift):
  new_text = ""
  for letter in encrypt_text:
    position = alphabet.index(letter)
    new_position = position-no_of_shift
    if new_position < 0:
      new_position += len(alphabet)
    new_text+=alphabet[new_position]
  print(new_text)
  
if direction == "decode":
  decrypt(text, shift)
else:
  encrypt(text, shift)
