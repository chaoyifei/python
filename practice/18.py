a=2
b=1
s=0
for n in range(1,21):
    s+=a/b
    t=a
    a=a+b
    b=t
print(s)