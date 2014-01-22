#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#http://ifram.ip138.com/ic.asp

import requests
from bs4 import BeautifulSoup
import re
import socket


import smtplib
from email.mime.text import MIMEText
import datetime
import time

class IP_PARSE_ERROR(Exception):
    def __init__(self):
        Exception.__init__(self)

class WhatIP(object):
    def __init__(self):
        self.preipinfo ='-1'
    
        self.ipinfo = '0'
    def getInnerIP(self):
        """
        Returns the actual ip of the local machine.

        This code figures out what source address would be used if some traffic
        were to be sent out to some well known address on the Internet. In this
        case, a Google DNS server is used, but the specific address does not
        matter much.  No traffic is actually sent.
        """
        try:
            csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            csock.connect(('8.8.8.8', 80))
            (addr, port) = csock.getsockname()
            csock.close()
            return addr
        except socket.error:
            #return "127.0.0.1"
            raise IP_PARSE_ERROR 

    def getIP(self):
        #raise IP_PARSE_ERROR 
        r= requests.get('http://iframe.ip138.com/ic.asp')
        if r.status_code == 200:
              soup = BeautifulSoup(r.content)
              #print soup.body.center.string
              #[\w:：]+\[([\d\.]+)\]\s[\w:：]+   
              matchs = re.search('\[([\d\.]+)\]',soup.body.center.string)
              if matchs:
                  return matchs.group(1)
        raise IP_PARSE_ERROR 
    def getIPInfo(self):
        try:
            self.ipinfo = 'LAN:%s\nWAN:%s'%(test.getInnerIP(),test.getIP())
            print self.ipinfo
        except Exception:
            raise IP_PARSE_ERROR 

    def mailIP(self):
        #ip有变化才发送邮件
        if self.ipinfo == self.preipinfo:
            return
        else:
            self.preipinfo = self.ipinfo
        mail_server = 'smtp.126.com'
        mail_port = 25
        mail_user =  'alladinfo@126.com'
        send_to = 'niwho@126.com'
        try:
            smtp_client = smtplib.SMTP(mail_server,mail_port)
            smtp_client.login('alladinfo@126.com','ADINFO')  

            today = datetime.date.today()
            msg = MIMEText( self.ipinfo )
            msg[ 'Subject' ] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
            msg[ 'From' ] =mail_user
            msg[ 'To' ] =send_to
            smtp_client.sendmail( mail_user, [send_to], msg.as_string() )
            
        except smtplib.SMTPException:
            print "send mail error."
        except Exception, what:
            print what 

    def listenIP(self):#监控ip变换，自动发送邮件
        while(1):
            try:
                self.getIPInfo()#可能会有异常
            except IP_PARSE_ERROR,what:
                print what
                time.sleep(60)#注意此函数以秒为单位
                continue
            except Exception, what:
                print what 
                time.sleep(60)#注意此函数以秒为单位
                continue
            #无异常则发送邮件
            self.mailIP()
            time.sleep(1)
            
if __name__ == '__main__':
    try:
        test = WhatIP()
        test.listenIP()
        #test.getIPInfo()
        #ipinfo = '%s,%s'%(test.getInnerIP(),test.getIP())
        #print ipinfo
        #print test.getInnerIP()
        #print test.getIP()
    except IP_PARSE_ERROR:
        print "获取系统外网IP失败！"#IP_PARSE_ERROR 
