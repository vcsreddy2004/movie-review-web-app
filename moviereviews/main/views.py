from django.shortcuts import render
from main.models import Movie,Review
import pickle as pkl
import os
from django.conf import settings
def home(req):
    moviesData = Movie.objects.all()
    return render(req,"index.html",{"movies":moviesData})
def movieViewPage(req,movieId):
    if req.method == "POST":
        review = req.POST['review']
        output = predict(review)
        data = Review(movieId=movieId,review=review,reviewOutput=output)
        data.save()
    movieData = Movie.objects.filter(movieId=movieId)[0]
    reviews = Review.objects.filter(movieId=movieId)
    return render(req,"movie-view-page.html",{"movieData":movieData,"reviews":reviews})
def predict(text):
    path = os.path.join(settings.BASE_DIR,"models","movie_reviews.pkl")
    with open(path, "rb") as file:
        model = pkl.load(file)
    output = ["negative","positive"]
    return output[model.predict([text])[0]]