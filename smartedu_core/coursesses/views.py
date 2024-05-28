from django.shortcuts import render
# from django.http import HttpResponse
from . models import Course, Category, Tag

def course_list(request):
    # return HttpResponse('<h1> INDEX SAYFASI </h1>')
    courses = Course.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses' : courses,
        'categories': categories,
        'tags':tags
    }


    return render(request,'courses.html', context) 


def course_detail(request, category_slug, course_id):
 
    course = Course.objects.get(category__slug=category_slug, id = course_id)
    categories = Category.objects.all()

    
    context = {
        'course': course,
      
    }

    return render(request, 'course.html', context)

def category_list(request, category_slug):
 
    courses = Course.objects.all().filter(category__slug= category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
    'courses' : courses,
    'categories': categories,
    'tags':tags
    }

    return render(request, 'courses.html', context)

def tag_list(request, tag_slug):
 
    courses = Course.objects.all().filter(tags__slug= tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses' : courses,
        'categories': categories,
        'tags':tags
    }

    return render(request, 'courses.html', context)