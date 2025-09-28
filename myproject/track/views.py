from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Track
# Create your views here.
def alltracks(request):
    # tracks=[[1,'python'],[2,'java'],[3,'c#']]
    tracks=Track.objects.all().order_by('id')
    return render(request,'list.html',context={'tracks':tracks})

def gettrackid(request):
    return HttpResponse("<h1>welcome to this track</h1>")

def inserttrack(request):
    print(request.POST)
    if request.method=='POST':
        name=request.POST['trackname']
        Track.objects.create(name=name)
        print(name)
        return redirect('alltracks')
    return render(request,'track_insert.html')

def updatetrack(request,id):
    track=Track.objects.get(id=id)
    if request.method=='POST':
        track.name=request.POST['trackname']
        track.save()
        return redirect('alltracks')
    return render(request,'track_update.html' ,context={'track':track})

def deletetrack(request,id):
    Track.objects.filter(id=id).delete()
    return redirect('alltracks')

def InactiveTrack(request, id):
    track = Track.objects.get(id=id)
    track.status = not track.status  # يعكس الحالة
    track.save()
    return redirect('alltracks')