n=int(input())
l=list(map(int,input().split()))
a=0
b=0
x=len(l)
for i in range(x):
    if i%2==0:
        a+=l[i]
print(a)