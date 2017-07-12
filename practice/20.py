def fun(n):
    if n==1 or n==0:
        return 1
    else:
        return fun(n-1)*n
print(fun(4))