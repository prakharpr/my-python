import wordlist as wordlist

generator = wordlist.Generator("1234567890")
for each in generator.generate(1, 10):
    print(each)
