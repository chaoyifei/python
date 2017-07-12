n=1
while n<=7:
    a=int(input('请输入一个数'))
    while a<1 or a>50:
        a=int(input('请输入一个数'))
    print(a*'*')
    n+1