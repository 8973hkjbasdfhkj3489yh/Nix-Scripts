#!/usr/bin/python3
#may also want to check ps auxf
import os
os.system("ls /proc/ > mmmur7")
lslist=[]
for i in open('mmmur7'):
    try:
        lslist.append(eval(i))
    except:
        pass
os.system("rm mmmur7")
for i in lslist:
    os.system("ps "+str(i))
    os.system("ls -lart /proc/"+str(i)+"/exe")
    os.system("ls -lart /proc/"+str(i)+"/cmdline")
    os.system("ls -lart /proc/"+str(i)+"/root")
    os.system("ls -lart /proc/"+str(i)+"/cwd")
    os.system("ls -lart /proc/"+str(i)+"/environ")
    os.system("ls -lart /proc/"+str(i)+"/fd")
    cmd = r'echo "\n\n\n\n"'
    os.system(cmd)
