def prime(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
b=list(map(int,input().split()))
c=0
for n in b:
    if prime(n)==1 and  n!=1:
        c+=1
print(c)