# Kilograms converter
# Richard Lefrandt, PROG 110 Python, 09/23/2018
# Hint: Use int() function to convert strings to integers
# and use str() function to convert numbers to strings.
# Look at the feetToMeters.py solution that I have posted in Module 1.

# Message Greeting "Welcome . . . "

print("Welcome to Pounds to Kilograms converter")

#Prompts the user to enter number of pounds

pounds = input("Enter the weight in Pounds: ")

#Calculates the equivalent kilograms using the formula:
kilograms = int(pounds)* 0.453592

print("Weight in Kilograms is: " + str(kilograms))

print("Goodbye!")
