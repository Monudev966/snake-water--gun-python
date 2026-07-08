#Snake,Water and Gun game
import random
'''
For Snake = -1
For Water = 0
For Gun = 1
'''
computer = random.choice([-1, 0, 1])
youstr=input("Enter your choice (S, W, G): ").lower()
youDict = {"s": -1, "w": 0, "g": 1}

you = youDict[youstr]

# So we have 2 variable by now, you and computer, now we will check the conditions for winning and losing
print(f"Computer chose: {computer}, You chose: {you}")

if computer == you:
    print("It is a draw")
else:
    if(computer == -1 and you== 1):
        print("You win!" )
    elif(computer == 1 and you== -1):
        print("You lose!")
    elif(computer == 0 and you== -1):
        print("You win!")
    elif(computer == -1 and you== 0):
        print("You lose!")
    elif(computer == 1 and you== 0):
        print("You win!")
    elif(computer == 0 and you== 1):
        print("You lose!")
    else:
        print("Invalid input! Please enter S, W, or G.")