import time

while True:
    str=input("enter a sentence \n")
    stri= input("enter a word \n")
    print("pracessing \n please wait")
    time.sleep(4)

    if(stri in str):
        print("{0} word is there in the sentence".format(stri))
    else:
        print("{0} word is not there in the sentence".format(stri))
        time.sleep(4)
