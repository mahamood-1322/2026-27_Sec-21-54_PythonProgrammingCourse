#python program to find the largest number in a series of N numbers entered by the user using for loop
N = int(input("Enter the value of N: "))
largest = None
for _ in range(N):
    num = int(input("Enter a number: "))
    if largest is None or num > largest:
        largest = num
print(f"The largest number is: {largest}")