#!/usr/bin/python3
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cipher(text, shift, direction):
  result = ""
  for letter in text:
    if letter not in alphabet:
        result+=letter
        continue
    position = alphabet.index(letter)
    if direction == "encode":
      new_position = position+shift
      if new_position > len(alphabet):
        new_position-=len(alphabet)
    else:
      new_position = position-shift
      if new_position < 0:
        new_position+=len(alphabet)
    result+=alphabet[new_position]
  print(result)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift%=26
    cipher(text, shift, direction)
    value = input("To continue enter 'yes' and to stop enter 'no'\n").lower()
    if value == "no":
        print("Goodbye")
        break
