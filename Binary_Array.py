n=int(input())
l=list(map(int,input().split()))
c=0
x=len(l)
for i in l:
    if i==0 or i==1:
        c+=1
if c==x:
    print(True)
else:
    print(False)
    