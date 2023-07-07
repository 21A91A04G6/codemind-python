n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if l.count(i)==i:
        c.append(i)
if len(c)>0:
    print(min(c),max(c))
else:
    print(-1)