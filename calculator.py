def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiplication(x,y):
    return(x*y)
def division(x,y):
    return(x/y)
def modulous(x,y):
    return(x%y)

print("Select opeartion:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulous")

while True:
    choice = input("Enter choice (1/2/3/4/5):")

    if choice in ('1','2','3','4','5'):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1 ,num2))

        elif choice =='3':
            print(num1, "*", num2, "=", multiplication(num1 ,num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1 ,num2))

        elif choice == '5':
            print(num1, "%", num2, "=", modulous(num1 ,num2))
            break
    else:
        print("Invalid Input")
            
  
            
   
            
    
