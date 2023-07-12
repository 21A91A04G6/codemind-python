n=input()
s=list(n)
c=0
l=("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ")
for i in s:
    if i not in l:
        c+=1
print(c)
