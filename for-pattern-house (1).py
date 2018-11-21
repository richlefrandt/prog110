#define function to draw a triangle of stars of size 9
def triangle(size):
    for n in range(1, (size+1),2):
        leading_spaces = (size - n)//2
        print(" "*leading_spaces+ "*"*n)

#define a new function to draw a rectangle pattern of size 9
# of dashes bordered by stars 
def rectangle(size):
    print((size)*"*")
    for n in range(1,size-1):
        print("*" + "-"* (size-2) + "*")
    print((size)*"*")

def house():
    size = int(input("Enter the size "))
    triangle(size)
    rectangle(size)

house()
