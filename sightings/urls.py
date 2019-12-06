from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('', views.index, name='index'),
    path('add/', views.add_squirrel, name='add'),
    path('stats/', views.stats, name='stats'),
    path('<str:unique_squirrel_id>/', views.edit_squirrel, name='edit'),
]
