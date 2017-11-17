#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2017/10/30 下午 15:34
@Author  : chaoyifei
@File    : test.py
@Software: PyCharm
'''
from communication import *
# 测试
if __name__ == '__main__':
    version='zeta-nix-all-2.6.0.9'
    version1='zeta-nix-2.6.0.9'
    dirname='/home/bigdata/'
    ip='10.20.66.230'
    plugin=''
    host=linux(ip,'bigdata','123456')
    host.connect()
    #杀进程
    host.send('cat %szeta/%s/pids/auth.pid | xargs kill' %(dirname,version1),'$')
    host.send('cat %szeta/%s/pids/daemon.pid | xargs kill' %(dirname,version1),'$')
    host.send('cat %szeta/%s/pids/master.pid | xargs kill' %(dirname,version1),'$')
    host.send('cat %szeta/%s/pids/worker.pid | xargs kill' %(dirname,version1),'$')
    # #删目录
    host.send('rm -rf %szeta*'%(dirname),'$')
    host.send_scp('scp root@10.20.66.122:/home/bigdata/%s.tar.gz /home/bigdata' %(version),'P@ssw0rd','$')
    #host.send('tar -zxvf /home/bigdata/zeta-nix-all-2.6.0.6.tar.gz -C /home/bigdata/test','$')
    host.send('tar -zxvf %s%s.tar.gz'%(dirname,version),'$')
    #修改配置文件
    host.send('sed -i \'s/^MASTER_WEB_HOST=.*/MASTER_WEB_HOST=%s/g\' %s%s/setting.env' %(ip,dirname,version),'$')
    host.send('sed -i \'s/^WORKER_HOST=.*/WORKER_HOST=%s/g\' %s%s/setting.env' %(ip,dirname,version),'$')
    host.send('sed -i \'s/^MASTER_HOST_INTERNAL=.*/MASTER_HOST_INTERNAL=%s/g\' %s%s/setting.env' %(ip,dirname,version),'$')
    host.send('sed -i \'s/master@127.0.0.1:9091/master@%s:9091/g\' %s%s/setting.env' %(ip,dirname,version),'$')
    host.send('sed -i \'s/^WORKER_HOST=.*/WORKER_HOST=%s/g\' %s%s/setting.env' %(ip,dirname,version),'$')
    host.send('sed -i \'s/^AUTH_INSTALL=.*/AUTH_INSTALL=1/g\' %s%s/setting.env' %(dirname,version),'$')
    host.send('sed -i \'s/^AUTH_HOST=.*/AUTH_HOST=%s/g\' %s%s/setting.env' %(ip,dirname,version),'$')
    host.send('sed -i \'s/^WORKER_PLUGINS=*/WORKER_PLUGINS=%s/g\' %s%s/setting.env' %(plugin,dirname,version),'$')
    host.send('sh %s%s/install.sh' %(dirname,version),'$')
    #host.send('ls -l','$')
    # host.send('java-version','$')
    host.close()



# 测试下载文件
# if __name__=='__main__':
#     host=linux('10.20.66.230','bigdata','123456')
#     host.sftp_down('/home/bigdata/zeta/zeta-nix-2.6.0.5/logs/worker-2017-11-08-0.log','E:\com\worker-2017-11-08-0.log')
# # 测试文件上传
# if __name__=='__main__':
#     host = linux('10.20.66.230', 'bigdata', '123456')
#     host.sftp_upload('E:\com\gdjson','/opt/test/gdjson')
#test
#test
