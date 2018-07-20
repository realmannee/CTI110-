# 71918
# CTI-110 P5HW2 - Random Number Guessing Game
# Roger Thompson
# create a simple  guess the number computer game in Python

def main():
 choice = 'y'

 while choice =='y':
    
    num = int(input("What is the secret number :"))

    if num > 777:
        print("Too high, try again")

    elif num < 777:
        print("Too low, try again")
   
    else:
        print("Congratulations, You have chosen the correct number!!")

    choice = input('Would you like to play again? ' 'y or n :')


main()
        
