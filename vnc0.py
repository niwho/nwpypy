# -*- coding: utf-8 -*- 
import imaplib
import rfc822,string,re,time,subprocess,email

class msg: # a file-like object for passing a string to rfc822.Message
    def __init__(self, text):
        self.lines = string.split(text, '\015\012')
        self.lines.reverse()
    def readline(self):
        try: return self.lines.pop() + '\n'
        except: return ''

class mailnw(object):
    def __init__(self):
        #self.imap = imaplib.IMAP4_SSL("imap.126.com")
        self.nwf=False
    def login(self,user,pwd):
        self.imap.login(user, pwd)
    def getconnectoin(self):
        self.imap = imaplib.IMAP4_SSL("imap.126.com")
        self.login('alladinfo@126.com', 'ADINFO')
        self.imap.select()
    def getMail(self):
        #self.login('alladinfo@126.com', 'ADINFO')self.imap.select()
        try: 
            r,data =self.imap.search(None,'(UNSEEN UNDELETED)')
            print 'data',data
        except :
            self.getconnectoin()
            r,data =self.imap.search(None,'(UNSEEN UNDELETED)')
        for num in data[0].split():
            try:
                f = self.imap.fetch(num, '(BODY[HEADER.FIELDS (SUBJECT FROM)])')
                #m = rfc822.Message(msg(f[1][0][1]), 0)
                #subject = m['subject']
            except KeyError:
                f = self.imap.fetch(num, '(BODY[HEADER.FIELDS (FROM)])')
                #m = rfc822.Message(msg(f[1][0][1]), 0)
                #subject = '(no subject)'
            subject = email.Header.decode_header(f[1][0][1])
            encoding_subject = subject[0][0]
            encoding = subject[0][1]

            if encoding is not None:
                subject = unicode(encoding_subject, encoding)
            else:
                subject = encoding_subject
        #encoding_subject = subject[0][0]
            print 'subject:%s'%(subject,)
            if re.search('Subject:\s*(.*vnc.*)', subject):
                self.nwf=True
                print 'have found'
                break
        #self.imap.close()
        #self.imap.logout()
    def run(self):
        while(1):
            print 'run...'
            self.getMail()
            if self.nwf:
                self.nwf=False
                #执行程序
                print 'call'
                subprocess.call(['c:/vnc.exe'])
            time.sleep(6)
            
if __name__ == "__main__":
    ml=mailnw()
    ml.run()
    #subprocess.call(['c:/vnc.exe'])
    #print 'exit....'
    
