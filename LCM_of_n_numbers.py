import math
n=int(input())
m=list(map(int,input().split()))
n1=m[0]
n2=m[1]
lcm=math.lcm(n1,n2)
for i in range(2,len(m)):
    lcm=math.lcm(lcm,m[i])
print(lcm)