n=int(input())
l=list(map(int,input().split()))
a=list()
b=list()
x=len(l)
for i in range(x):
    if i%2==0:
        a.append(l[i])
    else:
        b.append(l[i])
if sum(a)>sum(b):
    print(sum(a)-sum(b))
else:
    print(sum(b)-sum(a))