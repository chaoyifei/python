import random
a=[[random.randint(1,100) for i in range(3)] for j in range(3)]
b=[[random.randint(1,100) for i in range(3)] for j in range(3)]
print('a',a)
print('b',b)
c=a[:]
for i in range(len(a)):
    for j in range(len(a[i])):
        c[i][j]=a[i][j]+b[i][j]
print('c',c)