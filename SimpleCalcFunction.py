
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y==0:
        print("Error!")
    else:
        return x/y

def calculator ():
    while True:
        print("Select operation: ")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit")

        choice= input("Enter choice (1/2/3/4/5): ")
        if choice in ["1","2","3","4"]:
            x= float(input("Enter first number: "))
            y= float(input("Enter second number: "))

            if choice=="1":
                print(add(x,y))
            elif choice=="2":
                print(substract(x,y))
            elif choice=="3":
                print(multiply(x,y))
            elif choice=="4":
                print(division(x,y))
        elif choice=="5":
            print("Exit")
            break

calculator()

