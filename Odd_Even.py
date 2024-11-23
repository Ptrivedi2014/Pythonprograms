import time
while True:
    number = int(input("enter a number: \n"))
    print("processing ")
    print("please wait... \n")
    time.sleep(5)
    if(number % 2) == 0:
        print("{0} is even number".format(number))
    else:
        print("{0} is odd number".format(number))
    time.sleep(5)