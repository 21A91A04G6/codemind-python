n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    if i<0:
        i=-i
    i=str(i)
    i=list(i)
    d.append(len(i))
print(*d)
    