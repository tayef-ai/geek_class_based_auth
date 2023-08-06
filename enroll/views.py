from django.shortcuts import render, HttpResponsePermanentRedirect
from .forms import StudentRegistration
from .models import Student
from django.core import validators
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
@login_required(login_url='/login/')
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name = nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'enroll/addandshow.html', {'fm': fm, 'st': stud})

@login_required(login_url='/login/')
def delete_data(request, id):
    if request.method == 'POST':
        dt = Student.objects.get(pk=id)
        dt.delete()
        return HttpResponsePermanentRedirect('/enroll/')

@login_required(login_url='/login/')   
def edit_data(request, id):
    if request.method == 'POST':
        dt = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=dt)
        if fm.is_valid():
            fm.save()
            return HttpResponsePermanentRedirect('/enroll/')
    else:
        dt = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=dt)
    return render(request, 'enroll/updatestudent.html', {'fm': fm})    
