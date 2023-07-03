n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in l:
    if i%2!=0:
        a+=i
    else:
        b+=i
print(abs(a-b))