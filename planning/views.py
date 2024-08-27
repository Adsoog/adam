from django.http import HttpResponse
from projects.models import Project
from station.forms import StationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from station.models import Station

# Create your views here.
def planning_homepage(request):
    projects = Project.objects.prefetch_related('stations').all()
    context = {
        'projects': projects,
    }
    
    return render(request, 'planning_homepage.html', context)

def create_station(request, project_id):
    project = Project.objects.get(id=project_id)
    
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            station = form.save(commit=False)
            station.project = project
            station.save()
            return redirect(reverse('planning_homepage'))
    else:
        form = StationForm()

    context = {
        'form': form,
        'project': project
    }
    
    return render(request, 'create_station.html', context)

def station_detail(request, station_id):
    station = get_object_or_404(Station, id=station_id)
    photos = station.photos.all()
    documents = station.documents.all()
    attendance_records = station.attendance_records.all()
    
    context = {
        'station': station,
        'photos': photos,
        'documents': documents,
        'attendance_records': attendance_records,
    }
    
    return render(request, 'station_detail.html', context)