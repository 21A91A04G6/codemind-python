n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i not in c and i%2==0:
        c.append(i)
print(len(c))