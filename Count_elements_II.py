a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in n:
    if i not in c:
        c.append(i)
for j in m:
    if j not in d:
        d.append(j)
for i in c:
    if i not in d:
        e.append(i)
        
for i in d:
    if i not in c:
        e.append(i)


print(len(e))
        