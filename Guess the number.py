import random as r
x = r.randint(1, 100)
while True:
    try:
        user_input = input("Guess a number from 1 to 100          ")
        guess = int(user_input)
        if x > guess:
            print("Your guess is too low! Increase it !!!")
        elif x < guess:
            print("Your guess is too high! Decrease it !!!")
        else:
            print("Congrats 🎉🎊🎉🎊🎉🎊🎉\n You have guessed the number 👏👏👏")
            import random as r
            x = r.randint(1, 100)
            continue
    except ValueError:
        print("Enter valid number")
    
   

    
    
    
    
        
    
    
