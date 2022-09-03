from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="Select"),
    path('ques.html',views.questions,name="Questions"),
]