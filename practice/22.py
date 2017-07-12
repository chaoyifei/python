def fun(age,rank):
    if rank==1:
        return age
    else:
        return fun(age+2,rank-1)
print(fun(10,5))


