#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/09/15 下午 16:54
@Author  : chaoyifei
@File    : 1.py
@Software: PyCharm
'''
import paramiko
ip='10.10.100.59'
username='root'
passwd='Raysdata@2016'
def ssh2(ip,username,passwd,cmd):
    #paramiko.util.log_to_file('paramiko.log')
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=3)
        count = 0
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.readlines()
            count+=1
            print 'The unzip %s is OK\n' %(count)

            '''日志输出需重定向'''
            # for o in out:
            #     print o
        print ' unzip %s\tPASS\n'%(ip)
    except:
        print '%s\tError\n'%(ip)
if __name__=='__main__':
    cmd = ['unzip /home/bigdata/zeta-all-2.5.3.5.zip -d /home/bigdata/',\
           'unzip /home/bigdata/zeta-all-2.5.3.5/zeta-2.5.3.5.zip -d /home/bigdata/zeta-all-2.5.3.5/ '\
           '']#你要执行的命令列表
    #*******多线程留用********
    # username = raw_input()  #用户名
    # passwd = getpass()    #密码
    # threads = []   #多线程
    # print "Begin......"
    # for i in range(1,254):
    #     ip = '192.168.1.'+str(i)
    #       a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
    #       a.start()
    ssh2(ip,username,passwd,cmd)
