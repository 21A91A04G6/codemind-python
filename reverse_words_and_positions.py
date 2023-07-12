n=input().split()
c=[]
for i in n:
    x=i[::-1]
    c.append(x)
print(*c[::-1])
