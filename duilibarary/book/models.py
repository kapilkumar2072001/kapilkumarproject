from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class student(models.Model):
    roll=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    last=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.last}, {self.roll}"

    


# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()


    