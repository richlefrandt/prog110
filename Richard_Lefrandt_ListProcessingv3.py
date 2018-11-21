#Richard Lefrandt
#List Processing

"""program that computes asks the user for a set of integer numbers,
and does some processing on them.
"""

"""Write a program that prompts the user for integer number,
and using a while loop,


continues to prompt until user enters a 0.


--Program should store the numbers in a list.
It then calculates and prints the total and average of the numbers using a for-loop.
--Next it prompts the user for a number to be replaced in the list,
and prompts for the new number
that should replace that old number.
--Next it prints the list before replacing the number.
--It then replaces all instances of the old number in the list
with the new number, and prints the replaced list.
--Next it sorts the list, and prints the sorted list.
-Next it finds and prints the maximum number of the list.
"""
#Welcome message
print("Welcome to the List Processing program")

#Create a list for numbers to be stored in
mylist = []


number=int(input("Please enter next number (Enter 0 to end):"))

while number !=0:
    mylist.append(number)
    number=int(input("Please enter next number (Enter 0 to end):"))
    
totalnumbers =len(mylist)

print("the count of numbers:",totalnumbers)

sum = 0
#Caculate the totals of elements in the list
for x in mylist:
    sum += x


#Calculate and print the average
print('avg', sum / totalnumbers)
print("total numbers", sum) 


"""Prompt the user
for a number to be replaced in the list, and
prompts for the new number that should replace that old number
        returns the new number
    """
#Assign Old Number
oldNum = int(input('provide a number that is to be replaced in the list'))

#Assign New Number
newNum = int(input('provide new nubmber that replaces old number in the list'))

#returns the new number
print(newNum)

#prints the list before replaces the number
print(mylist)

#Replaces all instances of the old number with new number in the list
= mylist)

#Prints the replaced list




##while



##for
##
###Print Final Counts
##print("Count of numbers:", numCount)
##
##print(input("Total: numTotal , Averages:" ))
##
##print(input("Enter the old number to be replaced:"))
##
##print(input("Enter the new number:"))
##
##print("Before replacement")
##
##print("After replacement:")
##
##print("After sorting:")
##
##print("Maximum number in the list:")
##
##
##print("Good bye!")
##
##
##main ()
