# -*- coding: utf-8 -*-
'''
auth by lihuijie
Apr 5 2017
'''

import psutil
import urllib
import sendim

imList = "7415"
grList = ""
def sendMsg(msg):
    global imList
    global grList
    msg = urllib.quote(msg)
    sendim.SendImMsg(imList,msg,grList)

def cpuAlert():
    cpuP = psutil.cpu_percent(interval=0,percpu=False)
    cpuA = "CPUInfo: The Utilization of CPU In 3s: %s %%"%cpuP
    if int(cpuP) > 80:
        sendMsg(cpuA)
    print int(cpuP)

def memAlert():
    mem = psutil.virtual_memory()
    memT = mem.total
    memP = mem.percent
    memU = mem.used
    memA = """MemoryInfo: 
            The Total Memory Is %s MB
            The Used Memory Is %s MB
            The Percent of Used Memory Is %s %%"""%(memT/1024/1024,memU/1024/1024,memP)
    if int(memP) > 80:
        sendMsg(memA)
    print int(memP)

def diskAlert():
    disk = psutil.disk_usage('/')
    diskT = disk.total
    diskU = disk.used
    diskP = disk.percent
    diskA = """DiskInfo:
            The Total Disk Is %s GB
            The Used Disk Is %s GB
            The Percent of Used Disk Is %s %%"""%(diskT/1024/1024/1024,diskU/1024/1024/1024,diskP)
    if int(diskP) > 80:
        sendMsg(diskA)
    print int(diskP)


if __name__ == '__main__':
    cpuAlert()
    memAlert()
    diskAlert()