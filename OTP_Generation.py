n=input()
l=list(n)
a=[]
for i in range(len(l)):
    if (int(l[i])%2)!=0:
        a.append(str(int(l[i])*int(l[i])))
print(''.join(a))