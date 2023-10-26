from django.shortcuts import render
from .models import exercises

# Create your views here.
def home(request):
    return render(request, 'INDEX.html')

def partSelection(request):
    return render(request, 'partSelection.html')


def exercisesView(request, exercise):
    exerciseDetails = exercises.objects.get(part_name = exercise)
    return render(request, 'exercise.html',{'exercise': exerciseDetails})

def profile(request):
    return render(request, 'profile.html')