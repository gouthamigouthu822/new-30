from django.shortcuts import render
from django.http import HttpResponse
from app.models import *


def Topic_data(request):
    if request.method=='POST':
        tn=request.POST['Topic_name']
        t=Topic.objects.get_or_create(Topic_name=tn)[0]
        t.save()
        return HttpResponse('sucesss')
    return render(request,'Topic_data.html')
def Webpage_data(request):
    QST=Topic.objects.all()
    d={"one":QST}
    if request.method=='POST':
        tn=request.POST['Topic_name']
        na=request.POST['name']
        ur=request.POST['url']
        isn=Topic.objects.filter(Topic_name=tn)[0]
        isn.save()
        t=Webpage.objects.get_or_create(Topic_name=isn,name=na,url=ur)[0]
        t.save()
        return HttpResponse('sucessfully submited')
        # return HttpResponse('sucesss')
    return render(request,'Webpage_data.html',d)

def Acsess(request):
    QSW=Webpage.objects.all()
    r={"two":QSW}
    if request.method=='POST':
        na=request.POST['name_As']
        dt=request.POST['date_as']
        ist=Webpage.objects.filter(name=na)[0]
        ist.save()
        t=Acessrecord.objects.get_or_create(name=ist,date=dt)[0]
        t.save()
        
        return HttpResponse('sucessfully submited')
    return render(request,'Acsess.html',r)