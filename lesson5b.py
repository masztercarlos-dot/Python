# functions with parameters 
# example 1
def greetings(name) :
    print("Goodmorning", name)

# call the function 
greetings("carlos")

# example 2
def addition(num1, num2):
    answer= num1 +num2
    print("the sum is ", answer)

# call the function 
addition(60, 40)

# NB :a function is reusable block of codes  that perform a specific task
addition(900,700)
addition(1500,400)
addition(-160,-40)

# assignment
def subtraction(num1, num2):
    answer= num1 +num2
    print("the difference is ", answer)

# call the function 
subtraction(100 ,40)
    
# division 
def division(num1, num2):
    answer= num1 /num2
    print("the division is ", answer)

# call the function 
division(100 ,10)

# multiplication
def multiplication(num1, num2):
    answer= num1 *num2
    print("the multiplication is ", answer)

# call the function 
multiplication(100 ,10)

# simple interest 
def interest(P,R,T):
    answer= P * R * T/100
    print("the interest is ", answer)

# call the function 
interest(2000,20,2)


# Area of a triangle
def Area(b,h):
    answer= b*h *0.5
    print("the area is ", answer)

# call the function 
Area(50, 70)

# BMI
def BMI(w,h) :
    answer = w / h**2
    print(" the BMI is", answer)
#  call the formula
BMI(80,5)

