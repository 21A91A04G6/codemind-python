n=int(input())
l=list(map(int,input().split()))
d=[]
c=[]
for i in l :
    if i%2!=0:
        c.append(i)
    else:
        break
print(sum(c))