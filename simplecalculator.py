# Simple Calculator by Ankesh

# Taking input from user
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

print("Choose an operation: +, -, *, /")
operation = input("Enter the operation: ")

#Performing the calculation 

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Cannot divide by Zero 0."
    else:
        result = num1/num2
else:
    result = "Invalid operation"
    
# Displaying result
print("Result: ",result)
