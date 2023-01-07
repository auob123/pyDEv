from django.urls import path, include
from . import views

urlpatterns = [path('', views.Home, name='Home'),
               path('Востребованность.html', views.Востребованность, name='Востребованность'),
               path('География.html', views.География, name='География'),
               path('Навыки.html', views.Навыки, name='Навыки'),
               path('Последниевакансии.html', views.Последниевакансии, name='Последниевакансии'),

               ]
