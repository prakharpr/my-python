import imp
from ntpath import join
import random
import pyautogui

char = "abcdefghijklmnopqrstuvwxyz1234567890"
char_list = list(char)
password = pyautogui.password("Enter the password: ")

guess = ""
while guess != password:
    guess = random.choices(char_list, k=len(password))
    print(">>>>>>>>"+str(guess)+"<<<<<<<<")

    if guess == list(password):
        print("your password : " +"" .join(guess))
        break
