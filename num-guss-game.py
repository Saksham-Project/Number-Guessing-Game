'''
Number Guessing Game
'''
import random
    
ran_num = random.randint(1,100)
while True:
    user = input("Enter a number between 1 to 100('e' for exit):")

    if user == 'e':
        break
    try:
         user_choice = int(user)
    except:
        print("INVALID INPUT , Please enter a number or 'e' to exit.")
        continue
         
    if ran_num == user_choice:
        print("CONGRATULATION CORRECT ANSWER!")
        print("THANK YOU FOR PLAYING THE GAME 💐 ")
        break
    elif ran_num > user_choice:
        print(" Number Is Low,  Please Enter Greater Number.")
    elif ran_num < user_choice:
        print("Number Is High,  Please Enter Smaller Number.")
    
    
print("----GAME OVER----")


