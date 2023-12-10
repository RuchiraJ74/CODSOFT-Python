def add (num1, num2) :
    return num1 + num2

def sub (num1, num2) :
    return num1 - num2

def prod (num1, num2) :
    return num1 * num2

def div (num1, num2) :
    return num1 / num2

print("----Please choose which Arithmetic Operation you want to do----\n")
print("1. Addition\n")
print("2. Subtraction\n")
print("3. Multiplication\n") 
print("4. Division")

while True:

    select = int(input("Enter your Choice 1, 2, 3, 4 : "))

    n1 = int(input("Enter the 1 st number : "))
    n2 = int(input("Enter the 2 nd number : "))
        
    

    if select == 1:
        print(n1, " + ", n2, " = ", add(n1, n2))

    elif select == 2:
        print(n1, " - ", n2, " = ", sub(n1, n2))

    elif select == 3:
        print(n1, " * ", n2, " = ", prod(n1, n2))

    elif select == 4:
        print(n1, " / ", n2, " = ", div(n1, n2))

    else:
        print("Invalid Choice")


    ch = int(input("Do you wish to continue \n1. Yes \n2. No\n"))
    if ch == 2:
        break

    
    


