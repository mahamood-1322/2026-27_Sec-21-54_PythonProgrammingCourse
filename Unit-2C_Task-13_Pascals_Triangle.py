#python program to print Pascal's triangle
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()