n=int(input())
l=list(map(int,input().split()))
x=sorted(l,reverse=True)
if l==x:
    print("yes")
else:
    print("no")