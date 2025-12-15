import math
p=float(input("enter principal amount:"))
n=float(input("enter time in years :"))
r=float(input("enter rate of interest:"))
a = p*math.pow((1 + r/100),n)
print("compound interest is:",a)


