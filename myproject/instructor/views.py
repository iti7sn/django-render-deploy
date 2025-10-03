from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Instructor
from track.models import Track
# Create your views here.
def allinstructor(request):
    instructor=Instructor.getallinstructor()
    return render(request,'alltrainee.html',context={'instructor':instructor})

def getinstructorid(request):
    return HttpResponse("<h1>welcome to this instructor</h1>")

def insertinstructor(request):
    print(request.POST)
    context={}
    context['tracks']=Track.objects.all()
    if request.method=='POST':
        trackobj=Track.objects.get(id=request.POST['instructortrack'])
        if ('instructorphoto' in request.FILES):
            img=request.FILES['instructorphoto']
            Instructor.objects.create(name=request.POST['instructorname'],email=request.POST['instructoremail'],photo=img ,trackid=trackobj)
        else:
            Instructor.objects.create(name=request.POST['instructorname'],email=request.POST['instructoremail'],trackid=trackobj)
        return redirect('allinstructor')
    return render(request,'insert.html',context)
    

def updateinstructor(request,id):
    track=Track.objects.all()
    instructor=Instructor.getinstructorByid(id)
    if request.method=='POST':
        instructor.name=request.POST['instructorname']
        instructor.email=request.POST['instructoremail']
        instructor.trackid=Track.objects.get(id=request.POST['instructortrack'])
        if ('instructorphoto' in request.FILES):
            instructor.photo=request.FILES['instructorphoto']
        instructor.save()
        return redirect('allinstructor')
    return render(request,'update.html' ,context={'instructor':instructor ,'tracks':track})

def deleteinstructor(request,id):
    Instructor.getinstructorByid(id).delete()
    # Instructor.objects.filter(id=id).update(status=False)
    return redirect('allinstructor')

def Inactiveinstructor(request,id):
    # Instructor.objects.filter(id=id).delete()
    # Instructor.objects.filter(id=id).update(status=False)
    instructor=Instructor.objects.get(id=id)
    instructor.status=not instructor.status   # يعكس الحالة
    instructor.save()
    return redirect('allinstructor')



