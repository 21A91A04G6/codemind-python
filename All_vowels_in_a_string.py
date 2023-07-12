n=input()
l=("aeiou")
c=[]
for i in n:
    if i in l:
        if i not in c:
            c.append(i)
        
if len(c)==len(l):
    print(True)
else:
    print(False)
    
    