from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:question_id>/index/", views.index, name='index'),
    re_path(r'^vote', views.votes, name = 'join')

]
