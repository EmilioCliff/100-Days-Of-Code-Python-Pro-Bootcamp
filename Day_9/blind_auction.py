#!/usr/bin/python3
import os
from art import logo
bidder_log = {}
while True:
  print(logo)
  name = input("Enter your name: ")
  amount = int(input("Enter your bid: $"))
  bidder_log[name] = amount
  value = input("Is there another bidder? type 'yes' or 'no'.\n").lower()
  os.system("clear")
  if value == "no":
    break
highest = 0
winner = ""
for bidder in bidder_log:
  if highest < bidder_log[bidder]:
    winner = bidder
    highest = bidder_log[bidder]
print(f"The winner is {winner} with a bid of ${highest}")
