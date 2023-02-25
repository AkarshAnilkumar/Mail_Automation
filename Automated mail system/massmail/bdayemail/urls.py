from django.urls import path,include
from . import views
#from django.conf.urls import patterns,url

urlpatterns = [
    path('',views.sendBdayEmail,name='sendBdayEmail')
    #path('',views.sendSimpleMail,name='sendSimpleMail')
    #patterns('myapp.views',url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/''sendSimpleMail',ame='sendSimpleMail'),)
]