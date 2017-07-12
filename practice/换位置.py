a=[]
for i in range(6):
    a.append(int(input('num')))
b=sorted(a)
for j in range(6):
        if a[j]==b[0]:
            a[0],a[j]=a[j],a[0]
for k in range(6):
        if a[k]==b[5]:
            a[5],a[k]=a[k],a[5]
print(a)