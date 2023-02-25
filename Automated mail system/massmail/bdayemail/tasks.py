import csv
from datetime import *
from celery import shared_task
from django.core.mail import send_mail
from django.http import HttpResponse
from datetime import datetime

@shared_task(bind=True)
def sendSimpleMail(self):
    #emailto=['vidhyavjkumar05@gmail.com','vidhyavijayakumar12a13@gmail.com']
    emailto=[]
    email_file=open('email.csv','r')
    msg_file=open('message.txt','r')
    msg=msg_file.read()
    email=csv.reader(email_file)
    for row in email:
        print(row)
        bdate=row[2][:5]
        print(bdate+"Hello\n")
        print(datetime.now().strftime("%d-%m"))
        if datetime.now().strftime("%d-%m")==bdate:
            #name.extend(row[0])
            emailto.append(row[1])
    email_file.close()
    msg_file.close()
    res=send_mail('Happy Birthday!',msg,'test64sct@gmail.com',emailto,fail_silently=False)
    return HttpResponse("Mail sent successfully")
    # emailto=['vidhyavjkumar05@gmail.com','vidhyavijayakumar12a13@gmail.com']
    # res=send_mail('Testing mail','Hello! This is a test mail','test64sct@gmail.com',emailto,fail_silently=False)
    # return HttpResponse("Mail sent successfully")