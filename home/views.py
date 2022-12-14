from django.shortcuts import render
from django.http import HttpResponse
from home.models import *
from django.core.mail import send_mail
from .src import PersonResource
from tablib import Dataset
import pandas as pd


# import pywhatkit



# Create your views here.
def index(request):
  return (render(request, 'index.html'))

def view_stud_info(request):
  if(request.method=="POST"):
    sname = request.POST.get('sname')
    reg_no = request.POST.get('reg_no')
    mail = request.POST.get('mail')
    address = request.POST.get('address')
    taluka = request.POST.get('taluka')
    district = request.POST.get('district')
    taluka = request.POST.get('taluka')
    state = request.POST.get('state')
    view_stud_info = Student(address = address, taluka = taluka, district = district, state = state,sname=sname,reg_no = reg_no )
    view_stud_info.save()
    send_mail(
    'Regarding registration',
    'You have uploded your information sucessfully!',
    'sb082024@gmail.com',
    [mail],
    fail_silently=False,
   )

  return(render(request, 'student.html'))

def view_marks(request):
  if(request.method=="POST"):
    reg_no = request.POST.get('reg_no')
    subject = request.POST.get('subject')
    marks = request.POST.get('marks')
    semester = request.POST.get('semester')
    view_marks = Marks(reg_no = reg_no, subject = subject, marks = marks, semester = semester)
    view_marks.save()
  return(render(request, 'marks.html'))

def view_admission(request):
  return(render(request, 'admission.html'))

def view_feedback(request):
  return(render(request, 'feedback.html'))



def view_data(request):
  student_data = Student.objects.all()
  student_marks = Marks.objects.all()
  student_feedback = Feedback.objects.all()
  return render(request , 'view.html' , {'student' : student_data , 'marks' : student_marks , 'feedback' : student_feedback})
# Create your views here.


def abt(request):
  student_data = Student.objects.all()
  return render(request ,'stu.html' ,{'student' : student_data} )

def insert(request):
    Student = Student(sname=request.POST['sname'], reg_no=request.POST['reg_no'], address=request.POST['address'] ,taluka=request.POST['taluka'] ,district=request.POST['district'] ,state=request.POST['state'] )
    print("LOL")
    Student.save()
    return redirect('/')
  
 
  
def simple_upload(request):
  if request.method == 'POST':
    person_resource = PersonResource()
    dataset = Dataset()
    new_person = request.FILES('myfile')
    imported_data = dataset.load(new_person.read(), format='xlsx')
    for data in imported_data:
      value = Person(
        data[0],
        data[1],
        data[2],
        data[3]
      )
      value.save()
  return render(request, 'upload.html')