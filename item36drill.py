x = 5 # interger to variable
y = 5
z = 5
a = "sir johnathan" #string to variable
b = "sir wenselworth"
c = "sir javier"
a2 = 1.5 # float to variable
b2 = 2.5
c2 = 3.5 

print ("{} has {} apples and will eat {} of it".format(a,x,a2)) #format and print



def AppleEater(x): #definition
    if x-a2 > y-b2 and x-a2 > z-c2: #if/and statement as well as (-)
        print ("{} cannot eat more apples than {} and {}, therefore inferior".format(a,b,c))
    elif x == 0: #elif function
        print("{} was sick and the competition was cancelled".format(a))
    else:
        (x+y+z)%(a2+b2+c2) #addition, % and else statement
        print ("The peasants enjoy the leftover apples") 
#returns a string variable as well

AppleEater(5) #Call the function

PM = [1,2,3,4,5,6,7,8,9,10,11,12]

for x in PM: #For loop
    (x ++ 1)/2 #The ++ and / function
    print(x)


tuple1 = ("The Rock", 1988, "Triple H") #tuple

for x in tuple1: #tuple for looping
    print(x)

n = input("What's the best color?(It's purple)".lower())
while n != "purple": #While loop and the NOT clause
    print ("The correct answer should be Purple")
    n = input("What's the best color?")
    
