n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if l.count(i)==i:
        if i not in c:
            c.append(i)
if len(c)>0:
    print(*c)
else:
    print(-1)