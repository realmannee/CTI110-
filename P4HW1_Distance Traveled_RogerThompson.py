#CTI-110 
#P4HW1 - Distance Traveled
#Roger Thompson
#62818
# Ask user two questions: The speed of a vehicle,and number of hours it has traveled.
# Display the distance that the vehicle has traveled for each hour of that time period.

def main():
    choice = 'y'

    while choice =='y':

        #get # to get speed of vehicle
        speed = int(input('What is the speed of the Vehicle in MPH?'))

        #get # to get hours traveled
        hoursTraveled = int(input('How many hours traveled?'))

        # run for loop to get the total
        totalDistance = speed * hoursTraveled
        print('The distance traveled is :',totalDistance)

        # run for loop to get the total
        for x in range(1,hoursTraveled):
    
            print(x, x * speed)



        choice = input('Do you want to run this program again? ' 'y or n :')

main()    
     


