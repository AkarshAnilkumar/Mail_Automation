from django.shortcuts import render

import csv
from datetime import datetime
from django.shortcuts import render
from .tasks import sendSimpleMail
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def sendBdayEmail(request):
    # emailto=[]
    # email_file=open('email.csv','r')
    # msg_file=open('message.txt','r')
    # msg=msg_file.read()
    # email=csv.reader(email_file)
    # for row in email:
    #     print(row)
    #     bdate=row[2][:5]
    #     print(bdate)
    #     print(datetime.now().strftime("%d-%m"))
    #     if datetime.now().strftime("%d-%m")==bdate:
    #         #name.extend(row[0])
    #         emailto.append(row[1])
    #         print("done")
    # print(emailto)
    # email_file.close()
    # msg_file.close()
    # res=send_mail('Happy Birthday!',msg,'test64sct@gmail.com',emailto,fail_silently=False)
    # return HttpResponse("Mail sent successfully")
    sendSimpleMail.delay()
    return HttpResponse("Birthday message sent successfully!")

