#Richard_Lefrandt_paycheck Assignment
#Currency See p. 257 from Murach's Phython Programming, Ch 9
import locale as lc # *I don't know how to sue lc

# set the locale for use in currency formatting
lc.setlocale(lc.LC_ALL, "us") #*I don't know how to use lc.setlocale for currency, $ sign
starLine = '*' * 36

# Display a Welcome Message "Welcome to . . ."

print("Pay Check Calculator")

# Prompts the user to enter Hours Worked

hoursWorked = input("Enter Hours Worked: ")

# Prompts the user to enter Hourly Rate

hourlyRate = input("Enter Hourly Pay Rate: ")
#print("{}/hr").format(hourlyRate)###Not sure obviously how to include units.

print(starLine)

#Calculates the equivalent Gross Pay using the formula:
grossPay = float(hoursWorked) * float(hourlyRate)

#print("{}/hr").format(hourlyRate)###Not sure obviously how to include units.

taxRate = 18

taxAmount = grossPay * (taxRate / 100)

takeHomePay = grossPay - taxAmount

print("Hours worked:", hoursWorked, "", sep="\t| ")

#print(lc.currency("Pay Rate:", hourlyRate, "", sep="\t| ")) *I don't know how to use lc.currency!):

print("Pay Rate:", hourlyRate, "", sep="\t| ")

#print("${}").format(grossPay)###Not sure obviously how to include units.
print("Gross Pay:", grossPay, "", sep="\t| ")

print("Tax Rate:", taxRate, "", sep="\t| ")

print("Tax Amount:", taxAmount, "", sep="\t| ", end="\n")

print("Take Home Pay:", takeHomePay, "", sep="\t| ")

starLine = '*' * 36

print(starLine)


