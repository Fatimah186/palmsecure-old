# views.py

from django.shortcuts import HttpResponse
from .tests import capture_palm_print_frames
from django.shortcuts import render

def capture_frames_view(request):
    capture_palm_print_frames()
    return HttpResponse("Palm print captured and saved.")
def home_view(request):
    return render(request, 'home.html')



