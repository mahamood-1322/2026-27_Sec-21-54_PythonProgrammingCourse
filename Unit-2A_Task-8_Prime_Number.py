#python program to check whether a given number is prime or not
num = int(input("Enter a number: "))
is_prime = True
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")