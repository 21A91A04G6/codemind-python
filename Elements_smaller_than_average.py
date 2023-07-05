n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in l:
    c+=i
s=c//len(l)
for i in l:
    if i <=s:
        d+=1
print(d)