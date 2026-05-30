""" print("-- Calculator --")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Add:     ", a + b)
print("Sub:     ", a - b)
print("Mul:     ", a * b)
print("Div:     ", a / b) 

a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Choose + - * / : ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Can't divide by zero!")
    else:
        print(a / b)
else:
    print("Invalid choice")"""""

#solvebyharry
a=50
b=3
print("The value of", a, " + ", b, "is:", a+b)
print("The value of", a, " - ", b, "is:", a-b)
print("The value of", a, " * ", b, "is:", a*b)
print("The value of", a, " / ", b, "is:", a/b)
print("The value of", a, " % ", b, "is:", a%b)
