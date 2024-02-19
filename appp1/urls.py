from django.urls import path
from . import views

urlpatterns = [
    path('url/',views.happy,name = "happy"),
    path('url1/',views.happy2,name = 'happy2'),

]