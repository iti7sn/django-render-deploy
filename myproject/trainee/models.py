from django.db import models
from track.models import Track
# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(unique=True)
    photo=models.ImageField(upload_to='trainee/images',null=True)
    status=models.BooleanField(default=True)
    trackid=models.ForeignKey(Track,on_delete=models.CASCADE,default=1)

    @classmethod
    def getalltrainees(cls):
        return cls.objects.all().order_by('id')
    
    @classmethod
    def gettraineeByid(cls,id):
        return cls.objects.get(id=id)