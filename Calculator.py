def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error: Division by zero"
    return a/b
 
def calculator():   
    print("Choose an operation: ")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")

    while True:
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        option = int(input("Choose an operation: "))
        if option == 1:
            result=add(num1,num2)
        elif option == 2:
            result=subtract(num1,num2)
        elif option == 3:
            result=multiply(num1,num2)
        elif option == 4:
            result=divide(num1,num2)
        else:
            result = "Invalid operation"
        
        print(f"Result: {result}")
        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break
calculator()