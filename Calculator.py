import time
from itertools import count
for i in count ():    
    print ("Enter")
    print("1 for addtion")
    print("2 for substaction")
    print("3 for multiplication")
    print("4 for division")
    ch = int(input())
    if(ch<1):
        print("this number is not there in the list. try number from 1-4")
    if(ch > 0 & ch<5):
        print ("Entered option is", ch)
    if(ch==1):
        x=input("enter 1st number ")
        y=input("enter 2nd number ")
        z=int(x)+int(y)
        print("")
        print("processing \n please wait... \n")
        time.sleep(4)
        print ("sum =",z)
        time.sleep(4)
    if(ch==2):
        x=input("enter 1st number ")
        y=input("enter 2nd number ")
        z=int(x)-int(y)
        print("")
        print("processing \n please wait...\n")
        time.sleep(4)
        print ("difference =",z)
        time.sleep(4)
    if(ch==3):
        x=input("enter 1st number ")
        y=input("enter 2nd number ")
        z=int(x)*int(y)
        print("")
        print("processing \n please wait... \n")
        time.sleep(4)
        print ("product =",z)
        time.sleep(4)
    if(ch==4):
        x=input("enter 1st number ")
        y=input("enter 2nd number ")
        z=float(x)/float(y)
        print("")
        print("processing \n please wait... \n")
        time.sleep(4)
        print ("quotient =",z)
        time.sleep(4)
    if(ch>4):
        print("this number is not there in the list. try number from 1-4")
        time.sleep(4)
