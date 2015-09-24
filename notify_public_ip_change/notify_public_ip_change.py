#!/usr/bin/python

import urllib
import smtplib
import os


def change_current_ip(new_ip):
    fObj = open(os.path.join(os.path.dirname(__file__),'current_ip.txt'),'w')
    fObj.write(new_ip)
    fObj.close()


def check_ip_changed(new_ip):
    fObj = open(os.path.join(os.path.dirname(__file__),'current_ip.txt'),'r')
    current_saved_ip=fObj.readline()
    fObj.close()
    if current_saved_ip != new_ip:
        #Now that the IP has changed, update it as the current ip
        change_current_ip(new_ip)
        return True
    else:
        return False
    
 
# Fetch the Public ip address
new_ip=urllib.urlopen('http://ip.42.pl/raw').read()

#check is ip has changed. 
#Call check_ip_changed 
if check_ip_changed(new_ip) == True:
    sender = """ sender email address"""
    receiver = "Recipent email address """
    subject = "Alert!!! Public IP Changed for Home Network"
    message = 'Subject: %s\n\n New Public IP for home Network is %s' % (subject, new_ip)
    
    username = """ email address"""
    password = """ password """

    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.starttls()
    smtpObj.login(username,password)
    smtpObj.sendmail(sender, receiver, message)
    smtpObj.quit()
