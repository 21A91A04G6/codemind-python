n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in l:
    if i not in range(a,b+1):
        c+=i
print(c)