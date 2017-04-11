# -*- coding: utf-8 -*-
from pyDes import *
import base64
import time
import urllib

def desEncryptDecryt():
    key = [100,57,50,112,97,48,119,122]
    iv = [112,54,54,98,57,121,118,49]
    _key = ""
    for k in key:
        _key += chr(k)
    _iv = ""
    for i in iv:
        _iv += chr(i)
    d = des(_key, CBC, _iv, padmode=PAD_PKCS5)
    return d

def desEncrypt(inputstr):
    d = desEncryptDecryt()
    b = d.encrypt(inputstr)
    str2des = base64.b64encode(b)
    return str2des

def desDecryt(inputstr):
    d = desEncryptDecryt()
    des2str = d.decrypt(base64.b64decode(inputstr))
    return des2str

def SendImMsg(ims,msg,groupid):
	msg = "project_id=backup&digitids=%s&content=%s&groupid=%s"%(ims,msg,groupid)
	enmsg = desEncrypt(msg)
#	enmsg = enmsg.decode("utf-8")
	#外网地址
	url =  "http://10.32.64.24:10801/apie/im/sendmsg?apm_t=zst2c5of7760z9xq2jj3ws1v&apm_enc=%s"%enmsg
	#公网地址
	#url =  "http://113.106.204.102:10801/apie/im/sendmsg?apm_t=zst2c5of7760z9xq2jj3ws1v&apm_enc=%s"%enmsg
    #接口中控地址
    #url =  "http://apm.duoyioa.com/apie/im/sendmsg?apm_t=zst2c5of7760z9xq2jj3ws1v&apm_enc=%s"%enmsg
	urllib.urlopen(url)

if __name__ == '__main__':
	imid,msg,groupid = sys.argv[1:4]
	msg = urllib.quote(msg)
	SendImMsg(imid,msg,groupid)
