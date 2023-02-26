from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html')

def sendMail(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['msg']
        subject=name
        content='Name: '+name+'\nEmail: '+email+'\n\nMessage: '+msg
        emailto=['vidhyavijayakumar12a13@gmail.com']
        res=send_mail(subject,content,'test64sct@gmail.com',emailto,fail_silently=False)
        a='<button><a href="/">Home</a></button>'
        #return HttpResponse("Message sent!\n"+a)
        return render(request,'index.html')