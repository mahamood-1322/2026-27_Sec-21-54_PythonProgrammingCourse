#python program to demonstrate operator precedence and associativity
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))
result = x + y * z  # Multiplication has higher precedence than addition
print("Result:", result)