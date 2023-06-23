from django.shortcuts import render
from django.http import HttpResponse
from register.forms import NewUser


# Create your views here.
def index(request):
    return render(request,'index.html')

def user(request):
    sid=NewUser()
    if request.method=='POST':
        sid=NewUser(request.POST)
        if sid.is_valid():
            sid.save(commit=True)
            return index(request)
        else:
            print("error")
    return render(request,'user.html',{'vishen':sid})
