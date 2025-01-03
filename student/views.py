from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.


def setcookie(request):
    response= render(request,'student/setcookie.html')
    #response.set_cookie('username','Wasim Akram')
    #response.set_cookie('username','Wasim Akram',max_age=60)
    #response.set_cookie('username','Wasim Akram',expires=datetime.utcnow()+timedelta(days=2))
    
    #using signed cookies
    response.set_signed_cookie('username','Akram',salt='nm',expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):
    #name=request.COOKIES.get('username','Guest')
   
     #using signed cookies  { salt must be same in set and getcookie}
    name=request.get_signed_cookie('username','Guest',salt='nm')
    return render(request,'student/getcookie.html',{'data':name})

def delcookie(request):
    response= render(request,'student/delcookie.html')
    response.delete_cookie('username')
    return response


# Cookies Limitation
'''
• Each cookie can contain 4096 bytes Data
• Cookies can be stored in Browser and server
• It is sent with each request

'''