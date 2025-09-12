import random as r
while True:
    emojis = { 'r':'Rock', 's':'Scissors', 'p':'Paper' }
    choices = ('r', 'p', 's')
    user_choice = str(input("Choose Rock, Paper, Scissor (r/p/s)       ")).lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue
    computer_choice = r.choice(choices)
    print('you chose', emojis[user_choice])
    print('Computer chose', emojis[computer_choice])
    if computer_choice == user_choice:
        print("draw")
    elif computer_choice == 'r' and user_choice == 's':
        print("You lose!!!!")
    elif computer_choice == 'r' and user_choice == 'p':
        print("You win!!!!")
    elif computer_choice == 'p' and user_choice == 's':
        print("You win!!!!")
    elif computer_choice == 'p' and user_choice == 'r':
        print("You lose!!!!")
    elif computer_choice == 's' and user_choice == 'r':
        print("You win!!!!")
    elif computer_choice == 's' and user_choice == 'p':
        print("You lose!!!!")
    else:
        break
    
