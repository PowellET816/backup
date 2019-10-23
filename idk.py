# Ethan Powell
# period 6

# variable Declaration and assignment
myVariable = "Ethan" # string variable]
myNumber = 12 # int variable
myDecimal = 12.6 # float variable

# make a variable of type string
myVariable = "hi"

# while loops


x = 1
while x <= 10:
	print(x)
	x += 1
# challenge: make a while loop to count down from 100

x = 100
while x >= 1:
	print(x)
	x -= 1


# string concatenation
string1 = "Hello "
string2 = "World "
print(string1 + string2 + "!")

myVariable = "shrek"

string3 = "My favorite "
string4 = "movie is "
print(string3 + string4 + myVariable)

# input
# ex
yourName = input("What is your name? ")
print("Hello " + yourName)

favSong = input("What is your fav song? ")
print("i like " + favSong + " too")


# casting: changing one thing to another
myNum = input("Enter a number")
myNum = int(myNum) + 10
print("The answer is " + str(myNum))

# ask for 2 num, add them, print the sum

# if and if/else
myNum1 = input("Enter a number ")

myNum2 = input("Enter another number ")
myNum3 = myNum1 + myNum2
print("the answer is " + str(myNum3))

num = input("What is your number: ")

if num > 100:
	print("Your number is higher than 100 ")
elif num == 100:
	print("your num is 100")

bDay = input("Is today ur b-day ")
if bDay = "yes" 
print("happy bday")
else
print("haha")