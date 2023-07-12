n=int(input())
l=list(map(str,input().split()))
c=[]
b=[]
for i in l:
    i=str(i)
    n=list(i)
    x=len(n)
    c.append(x)
y=max(c)
for i in l:
    i=str(i)
    e=list(i)
    if len(e)==y:
        if i not in b:
            b.append(i)
print(*b)
