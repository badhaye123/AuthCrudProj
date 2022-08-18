from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from.forms import OrderForm
from .models import Orders
from django.contrib.auth.decorators import login_required


# Create your views here.
def testView(request):
    template_name='App1/base.html'
    context={}
    return render (request, template_name, context)


def AboutUsView(request):
    template_name='App1/aboutus.html'
    context={}
    return render (request, template_name, context)


def ContactUsView(request):
    template_name='App1/contactus.html'
    context={}
    return render (request, template_name, context)


@login_required(login_url='login')
def addorderView(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showorder')
            #return HttpResponse('order Placed')
    template_name='App1/addorders.html'
    context={'form':form}
    return render (request,template_name,context)

def showordersView(request):
    template_name='App1/showorders.html'
    ords=Orders.objects.all()
    context={'ords':ords}
    return render(request,template_name,context)

def updateorderView(request,id_from_fe):
    order=Orders.objects.get(id=id_from_fe)#Orders.objects.get(id=1)
    form=OrderForm(instance=order)#form filled with data from backend/database
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            print('Updated')
            return redirect('showorder')
    template_name='App1/addorders.html'
    context={'form':form}
    return render(request,template_name,context)

def deleteorderView(request,id_from_fe):
    order=Orders.objects.get(id=id_from_fe)
    order.delete()
    print('deleted')
    return redirect('showorder')









