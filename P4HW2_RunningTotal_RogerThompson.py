#CTI-110 
#P4HW2 - Running Total
#Roger Thompson
#62918
# Ask the user to enter a series of numbers which should loop and add those numbers to a
# running total, until the user enters a negative number.
# When a negative number is entered, have the program should exit the loop without adding
# the negative number to the total. Have the program then print the total before exiting.

def main():
    choice = 'y'

    while choice =='y':

        # initialize my accumlator to zero
        total = 0
        #get # of grades to total
        num = int(input("How many series of numbers would u like to total? "))

        #run for loop to get the total
        for x in range(1,num +1):

    
            print("Enter a number ",x,": ",sep="",end="")
            number = float(input())

            #number = float(input("Enter number: "))
            #total += number
            total = total + number 
            print("The number total is",format(total,',.0f'))


        choice = input('Do you want to run this program again? ' 'y or n :')

main()    
     
