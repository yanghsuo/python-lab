#该方法适合ping 连续的IP地址



# coding=utf-8

import os,time
import sys

start_Time=int(time.time())
ip_True = open('V2/ip_True.txt','w+')
ip_False = open('V2/ip_False.txt','w+')


IPhost = []
IPbegin = (input(u'请输入起始查询IP： '))
IPend = input(u'请输入终止查询IP： ')
IP1 = IPbegin.split('.')[0]
IP2 = IPbegin.split('.')[1]
IP3 = IPbegin.split('.')[2]
IP4 = IPbegin.split('.')[-1]
IPend_last = IPend.split('.')[-1]
count_True,count_False = 0,0




for i in range(int(IP4)-1,int(IPend_last)):
    ip = str(IP1+'.'+IP2+'.'+IP3+'.'+IP4)
    print('\n---------开始ping %s---------'%ip)
    int_IP4 = int(IP4)
    int_IP4 += 1
    IP4 = str(int_IP4)
    return1=os.system('ping -n 1  %s'%ip)
    if return1:
        print ('\033[1;7;30;42m ping %s is ok \033[0m'%ip)
        ip_False.write(ip+'\n')
        count_False += 1
    else:
        print ('\033[1;7;30;41m ping %s is fail  \033[0m'%ip)
        ip_True.write(ip+'\n')
        count_True += 1

ip_True.close()
ip_False.close()

end_Time = int(time.time())

print ("此次ping测试共耗时time(秒)：",end_Time - start_Time,"s")
print ("ping的ip总数：  ",count_True + count_False,"\nping通的ip数：  ",count_True,"\nping不通的ip数：",count_False)