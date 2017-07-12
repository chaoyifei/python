#coding:UTF-8
Tn=0
Sn=[]
n=int (input('n='))
a=int(input('a='))
for count in range(n):
    Tn=Tn+a
    a=a*10
    Sn.append(Tn)
    print(Tn)
Sn= (lambda x,y:x+y,Sn)

print ("和为：",Sn)