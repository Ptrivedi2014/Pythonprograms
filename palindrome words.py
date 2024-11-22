import time
while True:
    str=input("enter a word \n")
    print(str[::-1])
    if str==str[::-1]:
        print(str,"is palindrome")
    else:
        print(str,"is not palindrome")