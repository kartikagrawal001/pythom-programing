#GUESS THE NUMBER
import random
computer_num=random.randrange(1,101)
score=10
while True:
    user_num=int(input("guess the number between 1 to 100"))
    if user_num==computer_num:
        print("You Win With Score",score)
        break
    elif user_num<computer_num:
        print("Too Small")
    else:
        print("Too Large")
    score-=1
    
