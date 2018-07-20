# CTI-110 
# P3HW2 - Software Sales
# Roger Thompson
# 62618
# Enter the number of packages purchased,then display the amount of the discount
# Then the program should calculate total purchase cost with the discount applied.

# Total Cost 0.0
# Cost of package $99.00
# Discount percentage 10%,20%,30%,40%

# The cost of packages
packageCost =99
# Find the cost of packages
quantity = float(input( " Enter quantity of Packages sold :"))
# Package cost are 99.00
packageCost = packageCost * quantity
print (" The total cost of the packages is ", packageCost )

#find the discount

if quantity >0 and quantity <10:
    print ("0% discount")
     
elif quantity >9 and quantity <20:
    print ("10% discount")
 
elif quantity >19 and quantity <50:
    print ("20% discount")
  
elif quantity >49 and quantity <100:
    print ("30% discount")
   
else:
    print ("40% discount")
    
discount = 0.0    
discount = 0.1
discount = 0.2
discount = 0.3 
discount = 0.4
    
# Find the total discount of the Packages
discount = discount * packageCost
# Find the total cost of the Packages
totalCost = packageCost - discount
print (" The toalCost of the packages is ", totalCost)

