# -*- coding: utf-8 -*-
'''
auth by lihuijie
Apr 10 2017
'''

import os
import urllib
import sendim
import urllib2

imList = "7415,5951"
grList = ""
def sendMsg(msg):
    global imList
    global grList
    msg = urllib.quote(msg)
    sendim.SendImMsg(imList,msg,grList)


def restartIis():
    a_Path = "C:\Windows\System32\inetsrv"
    os.chdir(a_Path)
    i_Stop = os.system("appcmd stop apppool /apppool.name:project.oa.com")
    i_Start = os.system("appcmd start apppool /apppool.name:project.oa.com")
    i_Stop
    if int(i_Stop) == 0:
        stopMsg = "project.oa.com已经停止，正在重新启动..."
        sendMsg(stopMsg)
    i_Start
    if int(i_Start) == 0:
        startMsg = "project.oa.com重新启动完毕"
        sendMsg(startMsg)

def timeOut():
    count = 0
    while count < 5:
        try:
            response = urllib2.urlopen("http://jidi.oa.com/api/out/getpv", timeout=10)
        except :
            #print "timeout"
            count += 1
            warnMsg = "这是第%s次超时，再超时%s次就会重启站点 project.oa.com"%(count,5-count)
            sendMsg(warnMsg)
        else:
            #print "no error"
            if count == 0:
                count = 6
            else:
                recoverMsg = "project.oa.com 超时已经恢复，下次将重新计算超时"
                sendMsg(recoverMsg)
                count = 0
    if count == 5:
        #restartMsg = "正在重启..."
        #sendMsg(restartMsg)
        restartIis()
    elif count == 6:
        nothingMsg = "这次检测没有超时，来自project.oa.com检测"
        sendMsg(nothingMsg)




if __name__ == '__main__':
    timeOut()
    #restartIis()