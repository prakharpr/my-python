import random

char = "abcdefghijklmnopqrstuvwxyz1234567890"
char_list = list(char)
password = input("Enter a Password : ")

guess = ""
while (guess != password):
    guess=random.choices(char_list,k=len(password))
    guess="".join(guess)
print("your password : "+guess)    

