n=input()
l=("aeiou")
c=[]
d=[]
for i in n:
    if i in l:
        c.append(i)
for i in l:
    if i not in c:
        d.append(i)
if len(d)>0:
    print(*d)
else:
    print("0")