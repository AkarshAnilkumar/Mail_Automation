import csv
from django.core.mail import send_mail
from django.http import HttpResponse

def sendSimpleMail(request):
    #emailto=['vidhyavjkumar05@gmail.com','vidhyavijayakumar12a13@gmail.com']
    emailto=[]
    email_file=open('email.csv','r')
    msg_file=open('message.txt','r')
    msg=msg_file.read()
    email=csv.reader(email_file)
    for row in email:
        emailto.extend(row)  
        print(emailto)
    email_file.close()
    msg_file.close()
    res=send_mail('Testing mail',msg,'test64sct@gmail.com',emailto,fail_silently=False)
    return HttpResponse("Mail sent successfully")