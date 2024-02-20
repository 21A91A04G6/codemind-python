def sum(n):
    t=0
    for digit in str(n):
        t+=int(digit)
    return t
a=int(input())
l=list(map(int,input().split()))
t=0
for i in range(len(l)):
    t+=sum(l[i])
print(t)