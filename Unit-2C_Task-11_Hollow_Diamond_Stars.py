#python program to print a hollow diamond pattern of stars
rows = int(input("Enter the number of rows: "))
# Upper half of the diamond
for i in range(1, rows + 1):
    if i == 1:
        print(" " * (rows - i) + "*")
    else:
        print(" " * (rows - i) + "*" + " " * (2 * i - 3) + "*")
# Lower half of the diamond
for i in range(rows - 1, 0, -1):
    if i == 1:
        print(" " * (rows - i) + "*")
    else:
        print(" " * (rows - i) + "*" + " " * (2 * i - 3) + "*")