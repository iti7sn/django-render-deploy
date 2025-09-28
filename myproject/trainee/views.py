from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Trainee
from track.models import Track
# Create your views here.
def alltrainee(request):
    # trainee=[[1,'Ahmed','ahmed@email.com','photo'],[2,'Mohamed','mo@email.com','photo']]
    trainee=Trainee.getalltrainees()
    return render(request,'alltrainee.html',context={'trainee':trainee})

def gettraineeid(request):
    return HttpResponse("<h1>welcome to this trainee</h1>")

def inserttrainee(request):
    print(request.POST)
    # if request.method=='POST':
    #     name=request.POST['trname']
    #     email=request.POST['tremail']
    #     img=request.FILES['trphoto']
    #     Trainee.objects.create(name=name,email=email,photo=img)
    #     print(name,email,img)

    context={}
    context['tracks']=Track.objects.all()
    if request.method=='POST':
        trackobj=Track.objects.get(id=request.POST['trtrack'])
        if ('trphoto' in request.FILES):
            img=request.FILES['trphoto']
            Trainee.objects.create(name=request.POST['trname'],email=request.POST['tremail'],photo=img ,trackid=trackobj)
        else:
            Trainee.objects.create(name=request.POST['trname'],email=request.POST['tremail'],trackid=trackobj)
        return redirect('alltrainee')
    return render(request,'insert.html',context)
    

def updatetrainee(request,id):
    track=Track.objects.all()
    trainee=Trainee.gettraineeByid(id)
    if request.method=='POST':
        trainee.name=request.POST['trname']
        trainee.email=request.POST['tremail']
        trainee.trackid=Track.objects.get(id=request.POST['trtrack'])
        if ('trphoto' in request.FILES):
            trainee.photo=request.FILES['trphoto']
        trainee.save()
        return redirect('alltrainee')
    return render(request,'update.html' ,context={'trainee':trainee ,'tracks':track})

def deletetrainee(request,id):
    Trainee.gettraineeByid(id).delete()
    # Trainee.objects.filter(id=id).update(status=False)
    return redirect('alltrainee')

def Inactive(request,id):
    # Trainee.objects.filter(id=id).delete()
    # Trainee.objects.filter(id=id).update(status=False)
    trainee=Trainee.objects.get(id=id)
    trainee.status=not trainee.status   # يعكس الحالة
    trainee.save()
    return redirect('alltrainee')



