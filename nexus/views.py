from django.shortcuts import render

# Create your views here.
def nexus(request):
    return render(request, 'nexus.html')
    