#!/usr/bin/python3
import random
def generate_password():
    print("Welcome to my_password_generator")
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['@','!','(',')','[',']','\\','/',',','.','^','$']
    no_of_letters = int(input("Enter the number of letters you want in your password\n"))
    no_of_numbers = int(input("Enter the number of numbers you want in your password\n"))
    no_of_symbols = int(input("Enter the number of symbols you want i n your password\n"))
    password = []
    for _ in range(no_of_letters):
        password+=random.choice(letters)
    for _ in range(no_of_numbers):
        password+=random.choice(numbers)
    for _ in range(no_of_symbols):
        password+=random.choice(symbols)
    random.shuffle(password)
    password = "".join(password)
    print(password)
generate_password()
