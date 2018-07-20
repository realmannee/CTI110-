# CTI-110 
# P3HW1 - Age Classifier 
# Roger Thompson
# 62118
# Write a program that asks the user to enter a person’s age.
# Display a message indicating whether the person is an infant, a child, a teenager, or an adult.

age = int(input( " Enter a persons age :"))

if age >1 and age <13:
  print ("Person is an child")
  
elif age >12 and age < 20:
  print ("Person is an teenager")
 
elif age >19:
  print ("Person is an Adult")
 
else:
  print ("Person is a Infant")
