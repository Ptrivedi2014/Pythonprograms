import time

while True:
    nums = []
    length = int(input("enter the length of list\n"))
    print("Enter {0} elements ".format(length))
    for i in range(length):
        nums.append(int(input()))
    key=int(input("enter a key to search \n"))
    if(key in nums):
        print("{0} number is there in the list".format(key))
    else:
        print("{0} number is not there in the list".format(key))