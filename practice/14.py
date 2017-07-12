#coding:UTF-8
h=100
t=10
height=[]
for i in range(2,t+1):
    h/=2
    height.append(h)
print('第10次落地时，反弹%s高'%(min(height)/2))        # 第十次反弹为第十次落地距离的一半
print('第10次落地时，经过%s米'% (sum(height)*2+100))   # 总和加上第一次的 100
