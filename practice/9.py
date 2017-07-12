n=int(raw_input('please input a number'))
n1=n
l=[]
while n>1:
    for i in range(2,n+1):
        if n%i==0:
            n=n/i
            l.append(str(i))
            break
print('%d='%n1 + '*'.join(l))