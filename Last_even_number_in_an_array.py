n=int(input())
l=list(map(int,input().split()))
x=len(l)
for i in range(x):
    if l[i]%2==0:
        d=l[i]
print(d)