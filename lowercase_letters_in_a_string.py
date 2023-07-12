n=input()
s=list(n)
c=0
l=("qwertyuiopasdfghjklzxcvbnm")
for i in s:
    if i in l:
        c+=1
print(c)