from django.urls import path
from . import views # Imports the file called 'views' from the current directory.

urlMappings = [
    path('homepage/', views.home, name='homepage'),
]