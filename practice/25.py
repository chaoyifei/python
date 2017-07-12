import re
def judge(first,list):
    li=[]
    first=first.upper()
    for a in list:
        if re.match(first,a):
            li.append(a)
        print(li[0])
    else:
        second=input('请输入第二个字母：')
        for b in li:
            if re.match(first+second,b):
                print(b)
list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
first=input('请输入第一个字母')
judge(first,list)

