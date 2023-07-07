n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if l.count(i)==i:
        c.append(i)
if len(c)>0:
    x=(max(c)+min(c))/2
    print("%.2f"%x)
else:
    print(-1)