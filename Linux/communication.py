# -*- coding: utf-8 -*-
'''
@Time    : 2017/10/24 下午 22:09
@Author  : chaoyifei
@File    : communication.py
@Software: PyCharm
'''
import paramiko
from time import sleep
import re
# 定义一个类，表示一台远端linux主机
class linux(object):
    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self, ip, username, password, timeout=300, source_passwd = 'Raysdata@2016'):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport和chanel
        self.t = None
        self.chan=None
        # 链接失败的重试次数
        self.try_times=3
        self.source_passwd=source_passwd
    # 调用该方法连接远程主机
    def connect(self):
        while True:
            try:
                # 链接异常抛出
                self.t = paramiko.Transport(sock=(self.ip,22))
                self.t.connect(username=self.username, password=self.password)
                self.chan = self.t.open_session()
                self.chan.settimeout(self.timeout)
                self.chan.get_pty()
                self.chan.invoke_shell()
                # 连接正常
                print '连接%s成功' %(self.ip)
                # 接收到的网络数据解码为str
                print self.chan.recv(1024).decode('utf-8')
                return
            # 连接异常：
            except Exception, e1:
                if self.try_times != 0:
                    print e1
                    print '连接 % s失败，进行重试'% self.ip
                    self.try_times -= 1
                else:
                    print '重试3次失败，结束程序'
                    exit(1)
    # 断开连接
    def  close(self):
        self.chan.close()
        self.t.close()
    # 发送拷贝命令
    def send_scp(self,cmd,source_passwd,end_flag):
        self.result=''
        def back_display():
            while True:
                sleep(0.5)
                ret = self.chan.recv(1024)
                ret = ret.decode('utf-8')
                self.result += ret
                print ret
                if end_flag in ret:
                    return self.result
                    break
        cmd += '\r'
        #发送执行的命令
        self.chan.send(cmd)
        sleep(0.5)
        ret = self.chan.recv(1024)
        ret=ret.decode('utf-8')
        #?为提示秘钥
        if '?' in ret:
            self.chan.send('yes'+'\n')
            sleep(0.5)
            self.chan.send(source_passwd + '\n')
            sleep(0.5)
            back_display()
        #若提示密码
        else :
            self.chan.send(source_passwd+'\n')
            sleep(0.5)
            print self.chan.recv(1024)
            back_display()
    def send(self,cmd,end_flag):
        cmd += '\n'
        self.result=''
        # 通过命令执行提示符来判断命令是否执行完成
        self.chan.send(cmd)
        sleep(0.5)
        while True:
            sleep(0.5)
            ret=self.chan.recv(1024)
            ret=ret.decode('utf-8')
            self.result+=ret
            print ret
            if ret.endswith(end_flag):
                return self.result
            break

    #文件上传
    def sftp_upload(self,localpath,remotepath):
        try:
            self.t = paramiko.Transport(sock=(self.ip, 22))
            self.t.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(self.t)

            sftp.put(localpath=localpath,remotepath=remotepath)
            print '文件上传成功'
            self.t.close()
        except Exception, e:
            print 'error:'
            print e
            exit(1)
    # 文件下载
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

# 测试
if __name__ == '__main__':
    host=linux('10.20.66.230','bigdata','123456')
    host.connect()
    host.send('rm -rf zeta*','$')
    host.send_scp('scp root@10.10.100.57:/home/bigdata/zeta/target/zeta-nix-all-2.6.0.5.tar.gz /home/bigdata','Raysdata@2016','$')
    host.send('tar -zxvf /home/bigdata/zeta-nix-all-2.6.0.5.tar.gz -C /home/bigdata/test','$')
    #host.send('ls -l','$')
    #host.send('java-version','$')
    host.close()



# 测试下载文件
# if __name__=='__main__':
#     host=linux('10.20.66.230','bigdata','123456')
#     host.sftp_down('/home/bigdata/zeta/zeta-nix-2.6.0.5/logs/master-2017-11-01-0.log','E:\com\master-2017-11-01-0.log')
# 测试文件上传
# if __name__=='__main__':
#     host = linux('10.20.66.230', 'bigdata', '123456')
#     host.sftp_upload('E:\com\gdjson','/opt/test/gdjson')
#test
#test
