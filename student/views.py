from django.shortcuts import render

# Create your views here.


def setcookie(request):
    response= render(request,'student/setcookie.html')
    response.set_cookie('username','Wasim Akram')
    return response

def getcookie(request):
    name=request.COOKIES.get('username','Guest')
    return render(request,'student/getcookie.html',{'data':name})

def delcookie(request):
    response= render(request,'student/delcookie.html')
    response.delete_cookie('username')
    return response