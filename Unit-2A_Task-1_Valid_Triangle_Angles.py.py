#To check if the angles form a valid triangle
a = float(input("Enter the first angle: "))
b = float(input("Enter the second angle: "))
c = float(input("Enter the third angle: "))
if a > 0 and b > 0 and c > 0 and a + b + c == 180:
 print("The angle is valid triangle")
else:
  print("The angles not a valid triangle")