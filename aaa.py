__author__ = 'niwho'
"%a1%ba%fe"
g_a = "%e6%a3%80%e7%b4%a2%3a%e4%b8%ad%e5%9b%bd"
g_a = ["%e6%a3%80%e7%b4%a2%3a%e4%b8%ad%e5%9b%bd%e7%a7%91%e6%8a%80","%e4%b8%ad%e5%9b%bd%e7%a7%91%e6%8a%80",
       "%e4%b8%ad%e5%9b%bd%e7%a7%91%e6%8a%80","%e6%a3%80%e7%b4%a2%3a%e4%b8%ad%e5%9b%bd%e7%a7%91%e6%8a%80",
       "%E5%88%97%E8%A1%A8%E6%96%B9%E5%BC%8F"]
'''
http://epub.cnki.net/kns/oldnavi/n_list.aspx?NaviID=1&Field=cykm$%%22{0}%22&Value=%e4%b8%ad%e5%9b%bd%e7%a7%91%e6%8a%80&selectIndex=0&NaviLink=%e6%a3%80%e7%b4%a2%3a%e4%b8%ad%e5%9b%bd%e7%a7%91%e6%8a%80&ListSearchFlag=1&Flg=&DisplayMode=%E5%88%97%E8%A1%A8%E6%96%B9%E5%BC%8F


'''
import struct
class Parser(object):
    def __init__(self,ps):
        self.par_str = ps
    def doParse(self,*ll):
        #print "ddd"
        for par_str in ll:
            a = list(int(b,16) for b in par_str.split("%") if b)
            #print a
            #print "B"*a.__len__()
            print struct.pack("B"*a.__len__(),*a).decode("utf-8")
pp = Parser("g_a")
pp.doParse(*g_a)
