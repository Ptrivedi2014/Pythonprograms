while True:
    import random as r
    print("Welcome to roll the dice\n")
    x = input("roll the dice (y/n)   ")
    if x == "y" or x== "Y":
        dice1 = r.randint(1, 6)
        print("You rolled a ",dice1)
    elif x == "n" or x =="N":
        print("Thanks for playing")
        exit()
    else:
        print("Invalid choice\nchoose y or n\n")
        
    
        
        

        
        
        
    
