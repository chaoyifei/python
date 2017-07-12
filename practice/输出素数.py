a=int(input('输入最小值'))
b=int(input('输入最大值'))
for num in range(a,b+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)




