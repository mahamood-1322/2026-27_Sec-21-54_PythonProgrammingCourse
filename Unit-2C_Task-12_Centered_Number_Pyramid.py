#python program to print a centered pyramid pattern of numbers
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + str(i) * (2 * i - 1))