#TriangleDetector

#Message "Welcome to . . ."

print("Welcome to Triangle Detector")




#Message Prompts the user to enter
sideOne = int(input("Enter the length of a side of a triangle(a positive integer): "))

      
#Message Prompts the user to enter
sideTwo = int(input("Enter the length of a side of a triangle(a positive integer): "))


#Message Prompts the user to enter
sideThree = int(input("Enter the length of a side of a triangle(a positive integer): "))



#Mesage Output: if User input Valid and Invalid Comparisons: Equal: ==
#Not Equal: != Greater Than: > Less Than: < Greater or Equal: >= Less or
#Equal: <= Object Identity: is



if sideOne + sideTwo <= sideThree or sideOne + sideThree <= sideTwo or sideThree + sideTwo <= sideOne:
    print("It is an Invalid Triangle")
    
else:
    if sideOne == sideTwo == sideThree:
        print("It is an Equilateral Triangle")
    elif sideOne == sideTwo or sideTwo == sideThree or sideOne == sideThree:
        print("It is an Isosceles Triangle")
    else: 
        print("It is Scalene Triangle")


hypotenuse = max(sideOne, sideTwo, sideThree)

if sideTwo > hypotenuse:


if sideOne <= sideTwo <= sideThree:
elif sideTwo <= sideThree <= sideOne:
elif sideThree <= sideOne <= sideTwo:
elif ("It is a Right Angle Triangle")

elif

    sideOne + side
    #print("Good bye!")
