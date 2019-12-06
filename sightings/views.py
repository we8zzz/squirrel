from django.shortcuts import render, redirect
from .models import squirrel
from django.http import HttpResponse
from .forms import squirrelform

def index(request):
    squirrel_list = list(squirrel.objects.all())
    context = {'squirrel_list': squirrel_list}
    return render(request, 'sightings/index.html', context)

def edit_squirrel(request, unique_squirrel_id):
    squirrel_obj = squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)

    if request.method == 'POST':
        form = squirrelform(request.POST, instance=squirrel_obj)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = squirrelform(instance=squirrel_obj)
    context = {
            'form': form
            }
    return render(request, 'sightings/edit.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = squirrelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = squirrelform()
    context = {
            'form': form,
            }
    return render(request, 'sightings/edit.html' , context)

def stats(request):
    squirrel_list = list(squirrel.objects.all())
    count=len(squirrel_list)
    color_list=[0,0,0,0]
    gray = squirrel.objects.filter(primary_fur_color='Gray').count()
    cinnamon = squirrel.objects.filter(primary_fur_color='Cinnamon').count()
    black = squirrel.objects.filter(primary_fur_color='Black').count()
    color_unknown = squirrel.objects.filter(primary_fur_color='').count()
    ground_plane = squirrel.objects.filter(location='Ground Plane').count()
    above_ground = squirrel.objects.filter(location='Above Ground').count()
    location_unknown = squirrel.objects.filter(location='').count()
    context = {'squirrel_list': squirrel_list, 'count': count, 'gray': gray, 'cinnamon': cinnamon, 'black': black,
            'color_unknown': color_unknown, 'ground_plane': ground_plane, 'above_ground': above_ground, 
            'location_unknown': location_unknown}
    return render(request, 'sightings/stats.html', context)

def map(request):
    squirrel_list = list(squirrel.objects.all())[:100]
    context = {'sightings': squirrel_list}
    return render(request, 'sightings/map.html', context)
