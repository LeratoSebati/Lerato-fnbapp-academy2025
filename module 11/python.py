#numereic Data

num = 3

print(type(num))

num2 = 3.14

print(type(num2))

# int num = 3
# float num = 3

#variables

my_variable = 10
total_count = 0
user = 'lerato'

#invalid
second_variable = 10
user_name =20

#operatos

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# division (/)
# Modulus (%)
# Exponents(**)

x = 10
x -= 2

print(x)

#operators with strings

str1 = 'Hello'
str2 = 'world'

print(str1 + " " + str2 +" " +str2)

print(str1 * 3)

#Control statements

num = 0

if num > 0:
    print("this number is positive")
elif num == 0:
    print("This number is zero")
  
else:
    print("this number is negetive")
    
#Control statements

num1 =int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if num1 > num2:
    print(num1, "is greater than" , num2)
elif num2 > num1:
    print(num2, "is greater than" , num1)
else:
    print("this number is equal")
    
#Loops

#using the value loop to count from 1 to 5
count = 1

while count <= 5:
    print(count) 
    count += 1 # implements the count by 1
    
#Loop control statements

count = 0

while count <= 5:
    print(count) 
    count += 1 
    if count == 3:
        break # Exits the loop when the count is reached - 3