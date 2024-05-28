from django.urls import path
from . import views


urlpatterns = [

    path('', views.course_list, name="courses"),
    #path(route, view, opt(kısayol ismi)) içerir
      path('<slug:category_slug>/<int:course_id>', views.course_detail, name="course_detail"),
]