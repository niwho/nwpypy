#coding=utf-8
import requests
import json
import time
import sys
import logging

{"access_token":"77b4d16663umRlo4zCnFk24bEGsd1433","expires_in":1399135070,"time_left":86400,"uid":"3197136850","refresh_token":"26da316663umRlo4zCnFk24bEGs318f2"}
{"access_token":"6350796663umRlo4zCnFk24bEGs79a2c","expires_in":1399135589,"time_left":86400,"uid":"3197136850","refresh_token":"5cce726663umRlo4zCnFk24bEGs72e10"}
{"access_token":"8d4e3d6663umRlo4zCnFk24bEGs3d71f","expires_in":1399174101,"time_left":86400,"uid":"3197136850","refresh_token":"a5651d6663umRlo4zCnFk24bEGs1dbf7"}

poinfo = {
         'client_id': '4190850526',#1815bfd5409fd094c49eb12a803149a0
'client_secret':'d46aa6749b18c7d7d1e6545d7a6c5349' ,
'grant_type': 'authorization_code',
'code':'1815bfd5409fd094c49eb12a803149a0',
'redirect_uri':'http://wenxianbar.com/w/weipan'
#'refresh_token': '' 
  }

poinfo2 = {
    'client_id': '4190850526',#1815bfd5409fd094c49eb12a803149a0
'client_secret':'d46aa6749b18c7d7d1e6545d7a6c5349' ,
'grant_type': 'refresh_token',
"refresh_token":"5cce726663umRlo4zCnFk24bEGs72e10"
}

'https://upload-vdisk.sina.com.cn/2/files/sandbox/niwho?access_token=ca38176663umRlo4zCnFk24bEGs17e38'
'{"size":"71.61 KB","rev":"1310040912","thumb_exists":false,"bytes":"73331","modified":"Sat, 03 May 2014 09:00:26 +0000","path":"\/niwho","is_dir":false,"root":"sandbox","icon":"page_white","mime_type":"application\/octet-stream","revision":"1464390959","md5":"51512388aad6fc8a757bc41d96af5965","sha1":"2ac86d9b3d5f140809f6430e3f35434b69c9d9a8","is_deleted":false}'


class WeiPan(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger2 = logging.getLogger('niwho')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr = logging.FileHandler('weipan.log')
        hdlr2 = logging.FileHandler('weipan_info.log')
        hdlr.setFormatter(formatter)
        hdlr2.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger2.addHandler(hdlr2)
        
        stream_handler = logging.StreamHandler(sys.stderr)  
        self.logger.addHandler(stream_handler)
        self.logger2.addHandler(stream_handler)
        
        self.logger.setLevel(logging.DEBUG)
        self.logger2.setLevel(logging.DEBUG)
    
    def getAccessTokenWithCode(self,code):
        poinfo['code'] = code
        r = requests.post("https://auth.sina.com.cn/oauth2/access_token",data = poinfo)
        jn = json.loads(r.text)
        self.logger.info(str(jn))
        return jn
        if jn['access_token']:
            return jn['access_token'],jn['expires_in'],jn['time_left'],jn['refresh_token']
        else:
            return 'error',jn['code'],jn['msg']
    
    def getAccessTokenWithRefresh(self,refretoken):
        poinfo2['refresh_token'] = refretoken
        r = requests.post("https://auth.sina.com.cn/oauth2/access_token",data = poinfo2)
        jn = json.loads(r.text)
        self.logger.info(str(jn))
        return jn
        
    def lastLines(self,lines = 1,block_size=1024):
        f = open('weipan.log','r')
        f.seek(0, 2)
        block = ''
        start = 0
        #get seek position
        curpos = f.tell()
        while(curpos > 0): #while not BOF
            #seek ahead block_size+the length of last read block
            curpos -= (block_size + len(block));
            if curpos < 0: curpos = 0
            f.seek(curpos)
            #read to end
            block = f.read()
            nl_count = block.count('\n')
            #if read enough(more)
            if nl_count > lines: break
            #get the exact start position
        for n in range(nl_count-lines):
            n
            start = block.find('\n', start)+1
        f.close()
        #return block[start:]   
        return eval(block[start:][block[start:].find('INFO',0)+5:])   
    
    def getAccessToken(self):
        dit = self.lastLines()
        if dit['expires_in'] < int(time.time()):
            ret = wp.getAccessTokenWithRefresh(dit['refresh_token']) 
            return ret['access_token']
        return dit['access_token']
    
    def uploadFile(self,filepath='niwho'):
        #Content-Type: multipart/form-data;
        paths = []
        for pt in filepath.split('/'):
            paths.extend(pt.split('\\'))
        filename=paths[-1]
        url = 'https://upload-vdisk.sina.com.cn/2/files/sandbox/%s'%(filename,)
        params = {'access_token':self.getAccessToken()}
        #headers = {'content-type': 'multipart/form-data'}
        files = {'file': (filename, open(filepath, 'rb'))}
        r = requests.post(url,params =params ,files=files,verify=False)
        self.logger2.info(r.text)
        jn = json.loads(r.text)
        return jn
    
    def shareFile(self,filepath='niwho'):
        url = 'https://api.weipan.cn/2/shares/sandbox/%s'%(filepath,)    
        params = {'access_token':self.getAccessToken()}
        r = requests.post(url,params =params,verify=False)
        self.logger2.info(r.url)
        self.logger2.info(r.text)
        jn = json.loads(r.text)
        return jn
    
    def createFolder(self,path):
        url = 'https://api.weipan.cn/2/fileops/create_folder'
        data = {'root':'sandbox','path':path}
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
#par = {'client_id': '4190850526','redirect_uri':"http://wenxianbar.com/weipan"}
#r = requests.get('https://auth.sina.com.cn/oauth2/authorize',params =par)
#r = requests.post("https://auth.sina.com.cn/oauth2/access_token",data = poinfo2)
#print r.content
#jn = json.loads(r.text)
#for k,v in jn.items():
#    print k,v 
wp = WeiPan()
#refresh_token = wp.lastLines()['refresh_token']
#ret = wp.getAccessTokenWithRefresh(refresh_token)
#print ret 
print wp.getAccessToken()
#wp.uploadFile()
#wp.shareFile()
print wp.metadata('essy')
#print wp.createFolder('essy')


