while True:
    a = []
    length = int(input("How many numbers are there           "))
    try:
        for i in range(length):
            a.append(int(input("Enter element          ")))
        sum = sum(a)
        average = sum / length
        print(average)
    except ValueError:
        print("Invalid Choice!!!")
