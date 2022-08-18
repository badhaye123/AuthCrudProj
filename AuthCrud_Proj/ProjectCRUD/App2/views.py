from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginView(request):
    if request.method=='POST':
        u=request.POST.get('un')
        p=request.POST.get('pw')
        #return HttpResponse('Here write')
        user=authenticate(username=u,password=p)#1.user object=valid credentials
                                                 #2.None=Invalid Credentials
        if user is not None:
            print('Valid credentials')
            login(request,user)
            return redirect('showorder')
        else:
            print('Invalid credentials')
            messages.error(request,'Invalid credentials')
    template_name='App2/login.html'
    context={}
    return render(request,template_name,context)

def registerView(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            #return HttpResponse('Account Created!!')
    template_name='App2/register.html'
    context={'form':form}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')
