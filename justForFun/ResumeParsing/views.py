from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


# Create your views here.

def index(request):
    return render(request,'ResumeParsing/index.html')

def loginView(request):
    content = {}
    if request.method == 'POST':
        userName = request.POST['userName']
        userPassword = request.POST['userPassword']
        user = authenticate(username = userName, password = userPassword)
        if user is not None:
            login(request, user)
            message = 'Login Successfully';
            messageType = 'alert alert-success'
        else:
            message = 'Invalid Username and Password'
            messageType = 'alert alert-danger'

        content = {
                    'message':message,
                    'messageType':messageType
                }
    return render(request,'ResumeParsing/login.html', content)
