#coding=utf-8
import requests
import json
import time
import sys
import logging


class MyDropBox(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger2 = logging.getLogger('niwho')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr = logging.FileHandler('mydropbox.log')
        hdlr2 = logging.FileHandler('mydropbox_info.log')
        hdlr.setFormatter(formatter)
        hdlr2.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger2.addHandler(hdlr2)
        
        stream_handler = logging.StreamHandler(sys.stderr)  
        self.logger.addHandler(stream_handler)
        self.logger2.addHandler(stream_handler)
        
        self.logger.setLevel(logging.DEBUG)
        self.logger2.setLevel(logging.DEBUG)
    
    def getAccessToken(self):
        return '8uENdAWengkAAAAAAAAABpu6uYndAKyVGsdmFDGP-3Ju7YJFHKPyswuCJEz_2Tcg'
    
    def uploadFile(self,filepath='how-to-download-large-file-in-python-with-requests-py'):
        paths = []
        for pt in filepath.split('/'):
            paths.extend(pt.split('\\'))
        filename=paths[-1]
        url = 'https://api-content.dropbox.com/1/files_put/dropbox/essy/%s'%(filename,)
        params = {'access_token':self.getAccessToken()}
        data = open(filepath,'rb')
        data.seek(0,2)
        filesize = data.tell()
        data.seek(0,0)
        headers = {'Content-Length':filesize}
        r = requests.post(url,params =params ,data=data,headers=headers,verify=False)
        self.logger2.info(r.text)
        jn = json.loads(r.text)
        return jn
    
    def shareFile(self,filepath='how-to-download-large-file-in-python-with-requests-py'):
        url = 'https://api.dropbox.com/1/shares/dropbox/essy/%s'%(filepath,)    
        params = {'access_token':self.getAccessToken(),'short_url':True}
        r = requests.post(url,params =params,verify=False)
        self.logger2.info(r.url)
        self.logger2.info(r.text)
        jn = json.loads(r.text)
        return jn
    
    def createFolder(self,path):
        url = 'https://api.dropbox.com/1/fileops/create_folder'
        data = {'root':'dropbox','path':path}
        params = {'access_token':self.getAccessToken()}
        r = requests.post(url,params =params,data=data,verify=False)
        self.logger2.info(r.url)
        self.logger2.info(r.text)
        jn = json.loads(r.text)
        return jn
    
    def metadata(self,filename='niwho'):
        url = 'https://api.weipan.cn/2/metadata/sandbox/%s'%(filename,)    
        params = {'access_token':self.getAccessToken()}
        r = requests.get(url,params =params,verify=False)
        self.logger2.info(r.url)
        self.logger2.info(r.text)
        jn = json.loads(r.text)
        return jn

mdb = MyDropBox()
#print mdb.uploadFile()
print mdb.shareFile()

