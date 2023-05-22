import time
import xlrd
import os


#default.ini位置
# /Users/yangshuo30/Library/Application Support/VanDyke/SecureCRT/Config/Sessions/Default.ini

xlsx = xlrd.open_workbook('D:/python-lab/Lab-2/CRT.xls')
sheet1 = xlsx.sheets()[0]
rows = sheet1.nrows
cols = sheet1.ncols
all_content = []

# __________________创建ini文件，并将default内容复制到ini文件中_________________________

with open("D:/python-lab/Lab-2/Default.ini","r") as  d:
    default_ini = d.read()



def mkdir(site):
    folder = os.path.exists("D:/python-lab/Lab-2/test/"+site+'/')
    if not folder:
        print('in the folder')
        os.makedirs("D:/python-lab/Lab-2/test/"+site+'/')
    else:
        print("This file haved!")

    for name in range(rows):
        # host = sheet1.cell_value(name, 0)
        # ip = sheet1.cell_value(name,2)

        old_ini = os.path.exists("D:/python-lab/Lab-2/test/" + site + "/" + host + " " + ip + ".ini")
        if not old_ini:
            print('创建ini文件！')
            if not ip:
                print("This HOST is not set ip address:", host)
            else:
                ini = open("D:/python-lab/Lab-2/test/" + site + "/" + host + " " + ip + ".ini", "w")
                ini.write(default_ini)
                ###_________________________替换hostname______________________________________________________
                e = open("D:/python-lab/Lab-2/test/" + site + "/" + host + " " + ip + ".ini", "r")
                lines = e.readlines()
                flen = len(lines) - 1
                for i in range(flen):
                    if '"Hostname"=' in lines[i]:
                        lines[i] = lines[i].replace('"Hostname"=', '"Hostname"=' + ip)
                    with open("D:/python-lab/Lab-2/test/" + site + "/" + host + " " + ip + ".ini", "w") as n:
                        n.writelines(lines)

        else:
            print('ini文件已经存在！',)









for name in range(rows):
 #   row_content = []
    site = sheet1.cell_value(name, 1)
    host = sheet1.cell_value(name, 0)
    ip = sheet1.cell_value(name, 2)
    mkdir(site)


#_______________________________修改ini文件中的Hostname_______________________________
#
# for hostname in range(rows):
#     host = sheet1.cell_value(hostname, 0)
#     ip = sheet1.cell_value(hostname, 2)
#     if not ip:
#         print("this HOST is not set ip address:", host)
#     else:
#         print('start to change Hostname:',host)
#         e = open("/Users/yangshuo30/Desktop/test/" + site + "/" + host + " " + ip + ".ini", "r")
#         lines = e.readlines()
#         flen = len(lines) - 1
#         for i in range(flen):
#             if '"Hostname"=' in lines[i]:
#                 lines[i] = lines[i].replace('"Hostname"=', '"Hostname"='+ip)
#             with open("/Users/yangshuo30/Desktop/test/" + site + "/" + host + " " + ip + ".ini", "w") as  n:
#                 n.writelines(lines)




        #     e.write(line.replace('"Hostname"=','"Hostname"='+ip))
        # old = e.read()
        # new = old.replace('"Hostname"=','"Hostname"='+ip,)
        # with open("/Users/yangshuo30/Desktop/test/" + site + "/" + host + " " + ip + ".ini", "w") as f:
        #     f.write(new)
        # e.close()



#_________________测试--修改hostname



#
# with open("/Users/yangshuo30/Desktop/test/BJ-ALX爱立信/BJ-ALX-4F-AS01a 172.30.174.2.ini", "r") as t:
#         lines = t.readlines()
#         flen = len(lines)-1
#         for i in range(flen):
#             if '"Hostname"=' in lines[i]:
#                 lines[i]=lines[i].replace('"Hostname"=','"Hostname1111"=')
#             with open("/Users/yangshuo30/Desktop/test/BJ-ALX爱立信/BJ-ALX-4F-AS01a 172.30.174.2.ini", "w") as n:
#                 n.writelines(lines)



