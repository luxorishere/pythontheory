def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div (a, b):
    return a // b

def operation(a, b, op):
    if (op == 1):
        return add(a, b)
    elif op == 2:
        return sub(a, b)
    elif op == 3:
        return mult(a, b)
    else:
        return div(a, b)
    

def calculator():
    try:
        first = int(input("Enter the first number"))
        second = int(input("Enter the second number"))
        operator = int(input("Enter the 1, 2, 3, 4 to do\n1 -> add\n2 -> sub\n3 -> mult\n4 -> div"))
        second = operation(first, second, operator)
        print(second)
        check = int(input("Enter 1 to add the number or 0 to exit"))
        if check == 0:
            return second
        else:
            while (check == 1):
                first = int(input("Enter the number"))
                operator = int(input("Enter the 1, 2, 3, 4 to do\n1 -> add\n2 -> sub\n3 -> mult\n4 -> div"))
                second = operation(second, first, operator)
                print(second)

                check = int(input("Enter 1 to add the number or 0 to exit"))
            return second
    except:
        print("Error occoured somewhere in input")
        return -1
    
    
a = calculator()
print(a)
