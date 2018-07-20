# 7/19/2018
# CTI-110 P5HW1 - Test Average and Grade
# Roger Thompson
#Ask the user to enter five test grades,then display a letter grade for each score
#Finally the average test score.




def main():
    # initialize my accumlator to zero
    
    #get # of grades to total
    number = getInput()
    ave = getAverage(number)
    displayLetterGrade(ave)
    
def getAverage(number):
    total = 0
    #run for loop to get the total
    for x in range(1, number + 1):
        grade = float(input("Your test score is: "))
        #total += grade
        total = total + grade
    #print("The grade total is",format(total,',.0f'))

    ave = total / number
    return ave
    

def displayLetterGrade(ave):
    if ave > 89 and ave < 101:
        print("You made an A!")
        print("Your numeric grade of",ave,"is an A!")
    elif ave > 79 and ave < 90:
        print("You made an B!")
        print("Your numeric grade of",ave,"is an B!")
    elif ave > 69 and ave < 80:
        print("You made an C!")
        print("Your numeric grade of",ave,"is an C!")
    elif ave > 59 and ave < 70:
        print("You made an D!")
        print("Your numeric grade of",ave,"is an D!")
    elif ave >= 0 and ave < 60:
        print("You made an F!")
        print("Your numeric grade of",ave,"is an F!")
    else:
        print("Invalid input. Try again")
        
#function defintion to get the input
def getInput():
    num = int(input("Enter 5 test grades? "))
    return num
main()









