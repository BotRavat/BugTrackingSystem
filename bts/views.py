

from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from bts.models import AddBug
from bts.forms import BugRegistration

# Create your views here.

def btshome(request):
    if not request.user.is_authenticated:
         messages.error(request,'Please Login')
         return render(request,'home/loginpage.html')

    return render(request,'bts/btshome.html')



def bugreport(request):
    if not request.user.is_authenticated:
         messages.error(request,'Please Login')
         return render(request,'home/loginpage.html')
   # else :
    #    return render(request ,'bts/bugreport.html')
    show = AddBug.objects.all()
    return render(request,'bts/bugreport.html',{'show':show})


def updatebug(request,sno):
    if not request.user.is_authenticated:
         messages.error(request,'Please Login')
         return render(request,'home/loginpage.html')

    if request.method=='POST':     
        pi=AddBug.objects.get(pk=sno)
        fm=BugRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request,'bts/updatebug.html',{'form':fm,'show':pi})
    return redirect(bugreport)



def addbug(request):
    
    if not request.user.is_authenticated:
         messages.error(request,'Please Login')
         return render(request,'home/loginpage.html')       
    if request.method=='POST': 
        bugname=request.POST['bugname']
        bugdate=request.POST['bugdate']
        bugpriority=request.POST['bugpriority'] #name in html form is here - POST['bugpriority']
        content=request.POST['content']
        projectname=request.POST['projectname']
        username=request.POST['username']
        print(bugname,content )
        if len(bugname)<2 or not bugdate or not bugpriority or len(content)<4:
           messages.error(request,'Please fill the form correctly')
           return redirect('addbug')
        else:
            messages.success(request,'BUG added successfully')    
        addbug=AddBug(bugname=bugname,bugdate=bugdate,bugpriority=bugpriority,content=content)
        addbug.save()

    return render(request,'bts/addbug.html')    
     

  
def deletebug(request,sno):
    if not request.user.is_authenticated:
         messages.error(request,'Please Login')
         return render(request,'home/loginpage.html')

    if request.method=='POST':    
        pi=AddBug.objects.get(pk=sno)
        pi.delete() 
    
    return redirect(bugreport)




def bugdetail(request,sno):
    if not request.user.is_authenticated:
         messages.error(request,'Please Login')
         return render(request,'home/loginpage.html')

    if request.method=='POST':    
        show=AddBug.objects.get(pk=sno)
        return render(request,'bts/bugdetail.html',{'show':show})
    
    return redirect(bugreport)



def projectreport(request):
    if not request.user.is_authenticated:
         messages.error(request,'Please Login')
         return render(request,'home/loginpage.html')
    show = AddBug.objects.all()
    return render(request,'bts/showprojects.html',{'show':show})



def projectreportdata(request,projectname):
    if not request.user.is_authenticated:
         messages.error(request,'Please Login')
         return render(request,'home/loginpage.html')

    if request.method=='POST':
      name=projectname
      data=AddBug.objects.filter(projectname=name)
      return render(request,'bts/projectreport.html',{'key':data})
    return render(request,'bts/btshome.html')   




def addusers(request):
    if not request.user.is_authenticated:
         messages.error(request,'Please Login')
         return render(request,'home/loginpage.html')

    return redirect(request,'admin')





   