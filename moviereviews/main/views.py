from django.shortcuts import render
from main.models import Movie
def home(req):
    moviesData = Movie.objects.all()
    return render(req,"index.html",{"movies":moviesData})