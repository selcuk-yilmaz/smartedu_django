from django.urls import path
from pages.views import AboutView, IndexView


urlpatterns = [
    #path(route, view, opt(kısayol ismi))          >>>>>>function based olursa yapı bu
    # path('contact/', ContactView.as_view(), name="contact"),   >>>>>class based olursa  yapı bu
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),

]