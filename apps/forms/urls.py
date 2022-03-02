from django.urls import path
from apps.forms import views

urlpattern = [
    path('modelform/', views.form_modelform, name = "form_modelform")
]