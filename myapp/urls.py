from django.urls import path
from . import views

appname = 'myapp'

urlpatterns = [
    path('',views.index,name='index'),
]

