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
version='2.5.3.5'
def ssh2(ip,username,passwd):
    #paramiko.util.log_to_file('paramiko.log')
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=3)

        # for m in cmd:
        #     stdin, stdout, stderr = ssh.exec_command(m)
        #     out = stdout.readlines()
        #     count+=1
        #     print 'The  %s is OK\n' %(count)
        #
        #     '''日志输出需重定向'''
        #     # for o in out:
        #     #     print o
        print '  %s\tPASS\n'%(ip)
    except:
        print '%s\tError\n'%(ip)
    ssh.close()
# if __name__=='__main__':
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
            'unzip /home/bigdata/zeta-all-%%s/zeta-%%s.zip -d /home/bigdata/zeta-all-%s/'%(version),\
            'chmod -R 777 /home/bigdata/zeta-all-%s'%(version)]
conf_cmd=['sed -i \'s/127.0.0.1/10.10.100.59/g\' /home/bigdata/zeta-all-%%s/zeta-%s/conf/master.conf'%(version),\
          'sed -i \'s/^master.web.auth.host.*/master.web.auth.host = 127.0.0.1/g\' /home/bigdata/zeta-all-%%s/zeta-%s/conf/master.conf'%(version),\
          'sed -i \'s/127.0.0.1/10.10.100.59/g\' /home/bigdata/zeta-all-%%s/zeta-%s/conf/author.conf'%(version),\
          'sed -i \'s/127.0.0.1/10.10.100.59/g\' /home/bigdata/zeta-all-%%s/zeta-%s/conf/worker.conf'%(version),\
          'sed -i \'s/127.0.0.1/10.10.100.59/g\' /home/bigdata/zeta-all-%%s/zeta-%s/conf/daemon.conf'%(version)]
fire_cmd=['firewall-cmd --zone=public --add-port=6789/tcp --permanent',\
          'firewall-cmd --zone=public --add-port=9090/tcp --permanent',\
          'firewall-cmd --zone=public --add-port=9091/tcp --permanent',\
          'firewall-cmd --zone=public --add-port=19095/tcp --permanent',\
          'firewall-cmd --zone=public --add-port=9093/tcp --permanent',\
          'systemctl restart firewalld.service'
          ]
start_cmd=['sh /home/bigdata/zeta-all-%%s/zeta-%s/bin/start-auth.sh'%(version),\
           'sh /home/bigdata/zeta-all-%%s/zeta-%s/bin/start-master.sh'%(version),\
           'sh /home/bigdata/zeta-all-%%s/zeta-%s/bin/start-daemon.sh'%(version),\
           'sh /home/bigdata/zeta-all-%%s/zeta-%s/bin/start-worker.sh'%(version)
           ]

if __name__=='__main__':
    ssh2(ip, username, passwd)
    unzip(ip,username,passwd,unzip_cmd)
    conf(ip,username,passwd,conf_cmd)
    # fire(ip,username,passwd,fire_cmd)
    # start1(ip,username,passwd,start_cmd)