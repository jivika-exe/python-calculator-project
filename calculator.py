j = "calculator"
k = j.upper()
print(k.center(16, '-'))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Which operation do you want to perform (+, -, *, /): ")

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")