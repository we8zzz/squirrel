from django.urls import path
from . import views

urlpatterns = [
    path('sightings/', views.index, name='sightings'),
    path('map/', views.map, name='map'),
    path('sightings/add/', views.add_squirrel, name='add'),
    path('sightings/stats/', views.stats, name='stats'),
    path('sightings/<str:unique_squirrel_id>/', views.edit_squirrel, name='edit'),
]
