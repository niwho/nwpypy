#!/usr/bin/python  
# -*- coding: utf-8 -*-  

import smtplib
from email.mime.text import MIMEText
import datetime
import time

mail_server = 'smtp.126.com'
mail_port = 25
mail_user =  'alladinfo@126.com'
send_to = 'niwho@126.com'
def test():
    try:
        smtp_client = smtplib.SMTP(mail_server,mail_port)
        smtp_client.login('alladinfo@126.com','ADINFO')  

        today = datetime.date.today()
        msg = MIMEText( '192.168.12.45' )
        msg[ 'Subject' ] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
        msg[ 'From' ] =mail_user
        msg[ 'To' ] =send_to
        smtp_client.sendmail( mail_user, [send_to], msg.as_string() )
        
    except smtplib.SMTPException:
        print "send mail error."
    except Exception, what:
        print what 

test()
