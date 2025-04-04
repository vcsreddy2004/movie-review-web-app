from django.db import models

class Movie(models.Model):
    movieId = models.AutoField(primary_key=True)
    name = models.TextField()
    image = models.ImageField(upload_to="movie profile/")
class Review(models.Model):
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField()
    reviewOutput = models.BinaryField()