while True:
    try:
        sum = 0
        x = int(input("Enter till whare you want to add        "))
        for i in range(x):
            # print(i + 1)
            sum = sum + i + 1
        print(sum)    
    except ValueError:
        print("valueError")
            
            
    
