import os
import time
devices = ["192.168.146.11","192.168.146.12"]
find_str = '"Hostname"='
replace_str = ('"Hostname="1.1.1.1')

# print(type(find_str),find_str)
with open("D:/python-lab/Lab-2/Default.ini", "r") as d:  # 打开文件
    ini_default = d.read()
#     for ini_default in d.readlines(): # 读取文件
#         if find_str in ini_default:
#             print("find:",find_str)
#             ini_default = ini_default.replace(find_str, replace_str)
#             print(ini_default)
#         else:
#              d.close()

#
#
#

for ip in devices:
    with open("D:/python-lab/Lab-2/" + ip + ".ini","w+") as f:
        f.write(ini_default)


        find_str = '"Hostname="'
        replace_str = ('"Hostname="' + ip)

        for ini_default in f.readlines():
             if find_str in ini_default:
                print("it is in line")
                line = line.replace(find_str, replace_str)



#





