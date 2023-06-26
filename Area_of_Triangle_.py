import math as m
a,b,c=map(int,input().split())
s=(a+b+c)/2
x=s*(s-a)*(s-b)*(s-c)
ar=m.sqrt(x)
print("%.2f"%ar)