n=input().split()
a=("aeiouAEIOU")
b=[]
for i in n:
    c=0
    for j in i:
        if j in a:
            c+=1
    b.append(c)
print(b.count(min(b)))