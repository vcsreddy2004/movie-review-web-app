from django.shortcuts import render
from main.models import Movie,Review
def home(req):
    moviesData = Movie.objects.all()
    return render(req,"index.html",{"movies":moviesData})
def movieViewPage(req,movieId):
    movieData = Movie.objects.filter(movieId=movieId)[0]
    reviews = Review.objects.filter(movieId=movieId)
    return render(req,"movie-view-page.html",{"movieData":movieData,"reviews":reviews})