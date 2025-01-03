from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['username'] = 'Wasim Akram'
    request.session['lastname'] = 'Nasim Akram'
    request.session.set_expiry(60)  # session will expire in 60 seconds
    return render(request,'session/setsession.html')

def getsession(request):
    username = request.session.get('username')
    
    return render(request,'session/getsession.html',{'data':username})

#def delsession(request):
    #if 'username' in request.session:  # check if 'username' is in session
    #    del request.session['username']  # remove key 'username' from session
   # return render(request,'session/delsession.html')
    


def delsession(request):
    request.session.flush()
    request.session.clear_expired()  # remove all session data from the session
    return render(request,'session/delsession.html')












'''
                            Session
The session framework lets you store and retrieve arbitrary data on a per-site-visitor basis.
It stores data on the server side and abstracts the sending and receiving of cookies. Cookies contain a session ID not the data itself.
database-backed sessions - If you want to use a database-backed session, you need to add
'django.contrib.sessions' to your INSTALLED_APPS setting.
Once you have configured your installation, run manage.py migrate to install the single database table that stores session data.
file-based sessions - To use file-based sessions, set the SESSION_ENGINE setting to
"django.contrib.sessions.backends.file",
You might also want to set the SESSION_FILE_PATH setting (which defaults to output from tempfile.gettempdir, most likely /tmp) tò control where Django stores session files. Be sure to check that your Web server has permissions to read and write to this location.
cookie-based sessions - To use cookies-based sessions, set the SESSION ENGINE setting to
"django.contrib.sessions.backends.signed_cookies". The session data will be stored using Django's tools for cryptographic signing and the SECRET KEY setting.
cached sessions - For better performance, you may want to use a cache-based session backend. To store session data using Django's cache system, you'll first need to make sure you've configured your cache.
'''


'''flush - It deletes the current session data from the session and deletes the session cookie. This is used if you want to ensure that the previous session data can't be
accessed again from the user's browser (for example, the django.contrib.auth.logout) function calls
'''