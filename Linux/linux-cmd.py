#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/10/10 下午 15:28
@Author  : chaoyifei
@File    : linux-cmd.py
@Software: PyCharm
'''
import paramiko
import time
#定义通道
def linux_cmd(host_ip,username,password,timeouts,cmd,info,coun,end):
    #定义接收缓存大小
    recv_buffer = 1024
    # 设置ssh连接的远程主机地址和端口
    t = paramiko.Transport(host_ip, 22)
    # 设置登录名和密码
    t.connect(username=username, password=passwd)
    # 连接成功后打开一个channel
    chan = t.open_session()
    # 设置会话超时时间
    chan.settimeout(timeouts)
    # 打开远程的terminal
    chan.get_pty()
    # 激活terminal
    chan.invoke_shell()
    chan.send(cmd + '\n')
    time.sleep(2)
    strs = chan.recv(recv_buffer)
    print strs
    if info in strs:
        chan.send('yes' + '\n')
        time.sleep(2)
    else:
        pass
        chan.send(coun + '\n')
        str = chan.recv(recv_buffer)
        while not str.endswith(end):
            print  chan.recv(recv_buffer)
    t.close()