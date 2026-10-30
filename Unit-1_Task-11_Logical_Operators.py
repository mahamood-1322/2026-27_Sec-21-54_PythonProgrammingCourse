a=1
result = (a > 10) and (a < 10)   
print("result of",a,"> 10 and",a,"< 10 is",result)
a=20
result = (a > 3) and (a < 30)
print("result of",a,"> 3 and",a,"< 30 is",result)

a=5
result = (a > 10) or (a < 10)
print("result of",a,"> 10 or",a,"< 10 is",result)
a=20
result = (a > 30) or (a < 3)
print("result of",a,"> 30 or",a,"< 3 is",result)

a=5
result = not(a > 10)
print("result of not",a,"> 10 is",result)
a=20
result = not(a <40)
print("result of not",a,"< 40 is",result)