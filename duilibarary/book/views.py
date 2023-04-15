from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import student
# from django.urls import reverse


def homepage(request):

    std = student.objects.all()

    return render(request,"index.html",{'std': std})
def add_std(request):
    if request.method=='POST':
        print("Added")
        roll=request.POST.get("roll")
        name=request.POST.get("name")
        last=request.POST.get("last")

#create an object for moduls 
        s=student.objects.create(roll=roll,name=name,last=last)
        return redirect("/home")
    return render(request,"add.html")


def display(request):
    return(HttpResponse("done"))

def homePage(request):
    return HttpResponse()

def delete(request, id):
  s = student.objects.get(id=id)
  s.delete()
  return redirect('/home')


def update(request,id):
    if request.method=='POST':
        roll=request.POST.get("roll")
        name=request.POST.get("name")
        last=request.POST.get("last")
        student.objects.filter(id=id).update(roll=roll,name=name,last=last)    
    emp = student.objects.get(id=id)
    
    return render(request,"update.html",{'emp':emp})



def coursedetails(request,courseid):
    return(HttpResponse(courseid))


