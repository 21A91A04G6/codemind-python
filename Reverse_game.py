def rev(n):
    r=0
    while n!=0:
        d=n%10
        r=r*10+d
        n//=10
    return r
a=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(rev(i))
print(*c)