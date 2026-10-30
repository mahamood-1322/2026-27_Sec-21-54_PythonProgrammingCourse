#python program to print the multiplication table of a number
number = int(input("Enter a number: "))

print("\nMultiplication table using a for loop:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\nMultiplication table using a while loop:")
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1