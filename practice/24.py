a=input('请输入一串数字')
b=a[::-1]
if a==b:
    print('%s是回文' %a)
else:
    print('%s不是回文' %a)