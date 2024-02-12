def rev(n):
    r=0
    while n!=0:
        d=n%10
        r=r*10+d
        n//=10
    return r
a=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    b=rev(i)
    if i==b:
        c+=1
print(c)