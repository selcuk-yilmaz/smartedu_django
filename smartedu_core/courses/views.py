from django.shortcuts import render
# from django.http import HttpResponse
from . models import Course

def course_list(request):
    # return HttpResponse('<h1> INDEX SAYFASI </h1>')
    courses = Course.objects.all().order_by('-date')

    context = {
        'courses' : courses
    }


    return render(request,'courses.html', context) 
