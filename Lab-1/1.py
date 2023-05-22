import os
import time
import paramiko

ip = '192.168.146.10'
username = 'admin'
password = '1234567890'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # paramiko默认拒绝任何未知的public key，开启后接受未知的public key
ssh_client.connect(hostname=ip,username=username,password=password,look_for_keys=False)   # look_for_key默认是True，默认情况下在建立ssh链接前会查看本地是否存私钥。
command = ssh_client.invoke_shell()  #打开ssh会话

print('已成功登录交换机' + ip)

command.send('sys\n')

#配置loopback0的地址
# command.send('interface loop 0\n')
# command.send('ip address 1.1.1.1 32\n')
# command.send('quit\n' * 2)
# command.send('save\n')
# command.send('Y\n')
# time.sleep(2)


#配置SNMP
# command.send('snmp-agent \n'
#              'snmp-agent community read  public\n'
#              'snmp-agent sys-info version v2c v3\n')
# command.send('quit\n')
# command.send('save\n')
# command.send('Y\n')
# command.send('\n')
# time.sleep(2)

#command.send('ping 1.1.1.1\n')
# command.send_command('ping 1.1.1.1\n')
command.send('dis ip int brief\n')


output = (command.recv(65535000).decode('ascii'))
#output = (command.recv(65535).decode('ascii'))  #最多截屏长度65535bit
print(output)


ssh_client.close()