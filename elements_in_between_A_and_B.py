n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in l:
    if i in range(a,b+1):
        c.append(i)
if len(c)>0:
    print(*c)
else:
    print("-1")