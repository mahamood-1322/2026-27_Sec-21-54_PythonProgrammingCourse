#python program to find the largest of three numbers using nested if
a = 10
b = 20
c = 30

if a > b:
    if a > c:
        print("The largest number is:", a)
    else:
        print("The largest number is:", c)
else:
    if b > c:
        print("The largest number is:", b)
    else:
        print("The largest number is:", c)