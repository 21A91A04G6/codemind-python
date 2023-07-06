n=int(input())
l=list(map(int,input().split()))
res = 0
j = 0
for i in range(len(l), 0, -1):
    x = 2**j
    res += x*l[i-1]
    if(j > len(l)):
        break
    j += 1
print(str(res))