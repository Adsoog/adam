from django.shortcuts import render

# First view por te module Init
def welcome(request):
    return render(request, 'welcome.html')



def init(request):
    return render(request, 'init/init.html')

def interested(request):
    return render(request, 'interested/interested.html')
