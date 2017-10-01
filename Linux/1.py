#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/09/15 下午 16:54
@Author  : chaoyifei
@File    : 1.py
@Software: PyCharm
'''
import paramiko
import time
import sys
ip='10.20.66.230'
username='bigdata'
passwd='123456'
version='2.5.3.5'
source_ip='10.20.66.122'
source_path='/home/bigdata/zeta-all-%s.zip'%(version)
source_passwd='P@ssw0rd'
local_patch='/home/bigdata/'

#等待:


def CopyPakage(username,ip,passwd,source_ip,source_path,local_patch,source_passwd):
    recv_buffer=1024
    # 设置ssh连接的远程主机地址和端口
    t = paramiko.Transport((ip, 22))
    # 设置登录名和密码
    t.connect(username=username, password=passwd)
    # 连接成功后打开一个channel
    chan = t.open_session()
    # 设置会话超时时间
    chan.settimeout(300)
    # 打开远程的terminal
    chan.get_pty()
    # 激活terminal
    chan.invoke_shell()
    chan.send('scp root@%s:%s %s' %(source_ip,source_path,local_patch)+'\n')
    time.sleep(2)
    strs=chan.recv(recv_buffer)
    print strs
    if '?'in strs:
        chan.send('yes'+'\n')
        time.sleep(2)
    else:
        pass
        chan.send(source_passwd+'\n')
        str = chan.recv(recv_buffer)
        while not str.endswith('$'):
           print  chan.recv(recv_buffer)
    t.close()

# if __name__=='__main__':r
#     cmd = ['unzip /home/bigdata/zeta-all-2.5.3.5.zip -d /home/bigdata/',\
#            'unzip /home/bigdata/zeta-all-2.5.3.5/zeta-2.5.3.5.zip -d /home/bigdata/zeta-all-2.5.3.5/ '\
#            '']#你要执行的命令列表
    #*******多线程留用********
    # username = raw_input()  #用户名
    # passwd = getpass()    #密码
    # threads = []   #多线程
    # print "Begin......"
    # for i in range(1,254):
    #     ip = '192.168.1.'+str(i)
    #       a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
    #       a.start()
    # ssh2(ip,username,passwd,cmd)
#解压
def unzip(ip,username,passwd,unzip_cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=3)
        for m in unzip_cmd:
            print m
            stdin, stdout, stderr =ssh.exec_command(m)
            out = stdout.readlines()

        print ' %s unzip complete \n'%(ip)
    except:
        print '%s unzip fail\n'%(ip)
#修改配置文件
def conf(ip,username,passwd,conf_cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=3)
        for m in conf_cmd:
            print m
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.readlines()
        print ' %s 修改配置完成 \n'%(ip)
    except:
        print '%s 修改配置失败\n' %(ip)
#端口开放
def fire(ip,username,passwd,fire_cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=3)
        for m in fire_cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.readlines()
        print ' %s 特定端口开放成功 \n' % (ip)
    except:
        print '%s 特定端口开放失败\n' % (ip)
def start1(ip,username,passwd,start_cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=3)
        for m in start_cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.readlines()
        print ' %s 开启成功 \n' % (ip)
    except:
        print '%s 开启失败\n' % (ip)

unzip_cmd=['unzip /home/bigdata/zeta-all-%s.zip -d /home/bigdata/'%(version),\
            'unzip /home/bigdata/zeta-all-%s/zeta-%s.zip -d /home/bigdata/zeta-all-%s/'%(version,version,version),\
            'chmod -R 777 /home/bigdata/zeta-all-%s'%(version)]
conf_cmd=['sed -i \'s/127.0.0.1/%s/g\' /home/bigdata/zeta-all-%s/zeta-%s/conf/master.conf'%(ip,version,version),\
          'sed -i \'s/^master.web.auth.host.*/master.web.auth.host = 127.0.0.1/g\' /home/bigdata/zeta-all-%s/zeta-%s/conf/master.conf'%(version,version),\
          'sed -i \'s/127.0.0.1/%s/g\' /home/bigdata/zeta-all-%s/zeta-%s/conf/worker.conf'%(ip,version,version),\
          'sed -i \'s/127.0.0.1/%s/g\' /home/bigdata/zeta-all-%s/zeta-%s/conf/daemon.conf'%(ip,version,version)]
#cenos6.5
fire_cmd=['/sbin/iptables -I INPUT -p tcp --dport 6789 -j ACCEPT',\
          '/sbin/iptables -I INPUT -p tcp --dport 9090 -j ACCEPT',\
          '/sbin/iptables -I INPUT -p tcp --dport 9091 -j ACCEPT',\
          '/sbin/iptables -I INPUT -p tcp --dport 19095 -j ACCEPT',\
          '/sbin/iptables -I INPUT -p tcp --dport 9093 -j ACCEPT',\
          '/etc/rc.d/init.d/iptables save',\
          '/etc/init.d/iptables restart'
          ]
start_cmd=['sh /home/bigdata/zeta-all-%s/zeta-%s/bin/start-auth.sh'%(version,version),\
           'sh /home/bigdata/zeta-all-%s/zeta-%s/bin/start-master.sh'%(version,version),
           ]

if __name__=='__main__':
    CopyPakage(username,ip,passwd,source_ip,source_path,local_patch,source_passwd)
    #ssh2(ip, username, passwd)
    # unzip(ip,username,passwd,unzip_cmd)
    # conf(ip,username,passwd,conf_cmd)
    fire(ip,username='root',passwd='P@ssw0rd',fire_cmd=fire_cmd)
    # start1(ip,username,passwd,start_cmd)