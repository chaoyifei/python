while(1):
    n=int(input('请输入数'))
    print('运算结果为%d'%(pow(n,2)))
    if pow(n,2)<50:
        quit()
    else:
        print('请输入')
