#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/10/24 下午 22:09
@Author  : chaoyifei
@File    : communication.py
@Software: PyCharm
'''
import paramiko
import re
from time import sleep
import os
#定义一个类，表示一台远端linux主机
class linux(object):
    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self,ip,username,password,timeout=30):
        self.ip=ip
        self.username=username
        self.password=password
        self.timeout=timeout
        # transport和chanel
        self.t = None
        self.chan=None
        # 链接失败的重试次数
        self.try_times=3
    # 调用该方法连接远程主机
    def connect(self):
        while True:
            try:
                #链接异常抛出
                self.t = paramiko.Transport(sock=(self.ip,22))
                self.t.connect(username=self.username, password=self.password)
                self.chan = self.t.open_session()
                self.chan.settimeout(self.timeout)
                self.chan.get_pty()
                self.chan.invoke_shell()
                #连接正常
                print u'连接%s成功' %(self.ip)
                # 接收到的网络数据解码为str
                print self.chan.recv(65535).decode('utf-8')
                return
            #连接异常：
            except Exception,e1:
                if self.try_times!=0:
                    print '连接 % s失败，进行重试'% self.ip
                    self.try_times-=1
                else:
                    print u'重试3次失败，结束程序'
                    exit(1)
    #断开连接
    def close(self):
        self.chan.close()
        self.t.close()
    #发送命令
    def send(self,cmd):
        cmd+='\r'
        # 通过命令执行提示符来判断命令是否执行完成
        p = re.compile(r'$')
        result = ''
        #发送执行的命令
        self.chan.send(cmd)
        # 回显很长的命令可能执行较久，通过循环分批次取回回显
        while True:
            sleep(0.5)
            ret = self.chan.recv(65535)
            ret=ret.decode('utf-8')
            result+=ret
            if p.search(ret):
                print result
                return result

    #文件上传
    def sftp_upload(self,localpath,remotepath):
        try:
            self.t = paramiko.Transport(sock=(self.ip, 22))
            self.t.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(self.t)

            sftp.put(localpath=localpath,remotepath=remotepath)
            print '文件上传成功'
            self.t.close()
        except Exception,e:
            print 'error:'
            print e
            exit(1)
    #文件下载
    def sftp_down(self,remotepath,localpath):
        try:
            self.t = paramiko.Transport(sock=(self.ip, 22))
            self.t.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(self.t)

            sftp.get(remotepath=remotepath,localpath=localpath)
            print '下载文件成功'
            self.t.close()
        except Exception,e:
            print 'error'
            print e
            exit(1)

#测试
# if __name__ == '__main__':
#     host=linux('10.20.66.230','bigdata','123456')
#     host.connect()
#     host.send('ls -l')
#     host.close()
#测试下载文件
# if __name__=='__main__':
#     host=linux('10.20.66.230','bigdata','123456')
#     host.sftp_down('/home/bigdata/zeta/zeta-nix-2.6.0.2/logs/worker-2017-10-25-0.log','E:\com\worker-2017-10-25-0.log')
#测试文件上传
if __name__=='__main__':
    host = linux('10.20.66.230', 'bigdata', '123456')
    host.sftp_upload('E:\com\worker-2017-10-25-0.log','/home/bigdata/worker-2017-10-25-0.log')









