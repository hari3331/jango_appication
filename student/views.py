from django.http import HttpResponse
from django.shortcuts import render
from student.models import Student 
def home(request):
    
# Create your views here.
student=Student.objects.filter9=(fist_name = "hari")
return render(request,'home..html',{'s':Student})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')