n=int(input())
l=list(map(int,input().split()))
a=int(input())
c=0
for i in l:
    if i in range(a+1):
        c+=i
print(c)