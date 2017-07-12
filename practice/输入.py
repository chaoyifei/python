if __name__=='__main__':
    fs=open('test.txt','w')
    string=input('请输入字符串')
    string=string.upper()
    fs.write(string)
    fp=open('test.txt','r')
    print(fp.read())
    fp.close()