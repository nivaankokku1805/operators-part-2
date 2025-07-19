a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
    
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
    
#Activity 2 - not =

a = 10
b = 12
c = 12

print(a != b)      
print(b != c)

a = "Python"
b = "Coding"

if a != b:
    print(a, 'and',b,'are different')
    
a = 4
b = 5

if (a == 1) != (b == 5):
    print('Hello')
    
a = int(input("Enter a number"))

if a%2 != 0:
    print(a,"is not even number")         
    
    #Activity3 - BMI caculator
    
height = float(input("Enter your height in cm :"))
weight = float(input("Enter your weight in kg :"))
 
BMI = weight / (height/100)**2

print("Your BMI is ",BMI) 

if  BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severely over weight")
elif BMI <= 39.9:
    print("You are obese")  
else:
    print("You are severly obese")              
    
    