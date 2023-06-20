from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name = 'about'),
    path("education/", views.education, name ='education'),
    path("experience/", views.experience, name ='experience')

]