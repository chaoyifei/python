def encode(num):
    s=str(num)
    n=""
    for i in range(len(s)):
        n+=str((int(s[i])+5)%10)
    return int(n[::-1])
print(encode(1234))