n=int(input())
l=list(map(int,input().split()))
c=[]
m=[]
for j in l:
    if j not in c:
        c.append(j)
for i in c:
    m.append(i)
    m.append(l.count(i))
print(*m)