n=int(input())
l=list(map(int,input().split()))
c=0
d=0
x=l[0]
z=n//2
for i in l:
    if i in range(x,z+1):
        c+=i
    else:
        d+=i
print(abs(c-d))