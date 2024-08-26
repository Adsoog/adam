from django.shortcuts import render

# First view por te module Init
def init(request):
    return render(request, 'init/init.html')