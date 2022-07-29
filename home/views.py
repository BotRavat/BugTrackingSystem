from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.



def home(request):
  return render(request,'home/home.html')

def loginpage(request):
    return render(request,'home/loginpage.html')   

def signup(request):
    return render(request,'home/signup.html')   


def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None :
            login(request,user)
            return render(request,'bts/btshome.html')   
        else:
            messages.error(request,'Invalid Credentials Please try again')
            return redirect('loginpage')

    return HttpResponse('404- Not Found')    


def handlelogout(request):
    logout(request) 
    return redirect(home)


def contact(request):
    if request.method=='POST': 
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
       # print(name,email,phone,content )
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,'Please fill the form correctly')
            return redirect('contact')
        else:
            messages.success(request,'Your message has been sent')    
        contact=Contact(name=name,email=email,phone=phone,content=content)
        contact.save()

    return render(request,'home/contact.html')    

def about(request):
    return render(request,'home/about.html')   






