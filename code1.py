import hashlib

flag = 0

pass_hash = input("Enter md5 hash: ")
wordlist=input("enter your file name : ")
try:
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:
    encoded_word = word.encode('utf-8')
    digest = hashlib.md5(encoded_word.strip()).hexdigest()

    if digest == pass_hash:
        print("password found")
        print("password is:" + word)
        flag = 1
        break

    if flag == 0:
        print("password not in list you have given")
