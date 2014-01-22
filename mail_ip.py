#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#http://ifram.ip138.com/ic.asp

import requests
from bs4 import BeautifulSoup
import re
import socket

class IP_PARSE_ERROR(Exception):
    def __init__(self):
        Exception.__init__(self)

class WhatIP(object):
    def __init__(self):
        pass
    
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
            return "127.0.0.1"

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

if __name__ == '__main__':
    try:
        test = WhatIP()
        print test.getInnerIP()
        print test.getIP()
    except IP_PARSE_ERROR:
        print "获取系统外网IP失败！"#IP_PARSE_ERROR 
