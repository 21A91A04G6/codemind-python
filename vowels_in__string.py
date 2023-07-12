n=input()
c=[]
l=("aeiouAEIOU")
for i in n:
    if i in l:
        if i not in c:
            c.append(i)
print(*c)