n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if l[i]>l[i-1]:
        c+=1
if c+1==n:
    print("yes")
else:
    print("no")