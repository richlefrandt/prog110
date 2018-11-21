#paycheck, grossPay

#Sample table provided Tanuja Joshi, I tried to use for help with Pikachu Figure
#my attempt with limited time due to travel Chicago and behind compounded to not able to see follow along in class/forgot glasses.
#however need to turn in something.

starLine = '*' * 36

# Message "Welcome to . . ."

print("Pay Check Calculator")

# Prompts the user to enter Hours Worked

hoursWorked = input("Enter Hours Worked: ")

# Prompts the user to enter Hourly Rate

hourlyRate = input("Enter Hourly Pay Rate: ")

print(starLine)

#Calculates the equivalent Gross Pay using the formula:
grossPay = float(hoursWorked) * float(hourlyRate)

taxRate = 18

taxAmount = grossPay * (taxRate / 100)

takeHomePay = grossPay - taxAmount

print("Hours worked:", hoursWorked, "", sep="\t| ")

print("Pay Rate:", hourlyRate, "", sep="\t| ")

print("Gross Pay:", grossPay, "", sep="\t| ")

print("Tax Rate:", taxRate, "", sep="\t| ")

print("Tax Amount:", taxAmount, sep="\t| ", end="\n")

print("Take Home Pay:", takeHomePay, sep="\t| ", end="\n")

starLine = '*' * 36

