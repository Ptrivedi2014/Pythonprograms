import time

while True:
    str=input("enter a sentence \n")
    stri=str.split(" ")
    stri=stri[-1::-1]
    print("processing \n please wait")
    time.sleep(4)
    print(stri)
    time.sleep(4)