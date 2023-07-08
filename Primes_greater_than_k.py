def prime(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
l=list(map(int,input().split()))
b=int(input())
c=0
for n in l:
    if prime(n)==1 and  n!=1 and n>=b:
        c+=1
print(c)