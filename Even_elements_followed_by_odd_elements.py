n=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in l:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
e=c+d
print(*e)