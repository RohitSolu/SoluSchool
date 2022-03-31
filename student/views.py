from re import template
from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from .models import Student, Subject,Result,Issuer
from .forms import SearchForm, StudentForm, SubjectForm, ResultForm,IssuerForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q 
from django.db.models import Avg
# from pathlib import Path
# import sys
from weasyprint import HTML
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'student/index.html')

@login_required
def home(request):
    return render(request,'student/home.html')

#Auth
class SignUp(LoginRequiredMixin, generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


#Student
@login_required
def student_1(request,id):
    students = Student.objects.filter(cls=id)
    page = request.GET.get('page', 1)
    paginator = Paginator(students, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'students': students,
        'users': users
        }
    return render(request, 'student/student_1.html',context)


@login_required
def addStudent(request):
    template = 'student/addStudent.html'
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {"form": form}
    return render(request, template, context)

@login_required
def student_update(request, pk):
    template = 'student/student_update.html'
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {"form": form}
    return render(request, template, context)

@login_required
def student_delete(request, pk):
    template = 'student/student_delete.html'
    obj = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    context = {"book": obj}
    return render(request, template, context)

#Subject
@login_required
def subject(request, id):
    subjects = Subject.objects.filter(cls=id)
    context = {
        'subjects': subjects,
        }
    return render(request, 'subject/subject_1.html',context)

@login_required
def addSubject(request):
    template = 'subject/addsubject.html'
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {"form": form}
    return render(request, template, context)
@login_required
def subject_update(request, pk):
    template = 'subject/subject_update.html'
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(request.POST or None, instance=subject)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {"form": form}
    return render(request, template, context)
@login_required
def subject_delete(request, pk):
    template = 'subject/subject_delete.html'
    obj = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    context = {"book": obj}
    return render(request, template, context)
#Result
@login_required
def result_1(request, id):
    results = Result.objects.filter(name__cls=id)
    context = {
        'results': results,
        }
    return render(request, 'result/result_1.html',context)

@login_required
def addResult(request):
    template = 'result/addresult.html'
    form = ResultForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {"form": form}
    return render(request, template, context)
    return render(request, 'result/addresult.html', {'form':form})

#Search
@login_required
def searchview(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query) | Q(registration_number__icontains=query)

            students= Student.objects.filter(lookups).distinct()

            context={'students': students,
                     'submitbutton': submitbutton}

            return render(request, 'search/search_result.html', context)

        else:
            return HttpResponse("Please enter the name of student.")

    else:
        return HttpResponse("Please Use Valid Search Method.")
@login_required
def marksheet(request, roll_no):
    student = Student.objects.get(roll_no=roll_no)
    avgs = Result.objects.values('subject__name').annotate(avg1=Avg('grade_point'))
    results = student.result_set.all()
    sum=0
    countr = 0
    for result in results:
        print(result.grade_point)
        sum=(sum+result.grade_point)
        countr = countr+1

    avg = sum/countr
    print(avg)
    # avgs = student.result_set.all.aggregate(avg1=Avg('grade_point'))
    issuers = Issuer.objects.all()
    context = {
        'results': results,
        'issuers': issuers,
        'avgs':avg,
    }
    return render(request,'student/marksheet.html',context)

#Dashboard
class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard/dashboard.html"
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['students'] = Student.objects.count()
        context['subjects'] = Subject.objects.count()
        context['results'] = Result.objects.count()
        return context

#Issuer

@login_required
def issuer(request):
    issuers = Issuer.objects.all()
    context = {
        'issuers': issuers,
        }
    return render(request, 'issuer/issuer.html',context)

@login_required
def issuer_update(request, id):
    template = 'issuer/issuer_update.html'
    issuer = get_object_or_404(Issuer, id=id)
    form = IssuerForm(request.POST or None, instance=issuer)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {"form": form}
    return render(request, template, context)