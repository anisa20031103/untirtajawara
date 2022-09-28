from django.shortcuts import render

# Create your views here.
def indexhome(request):
    return render(request, 'home.html')