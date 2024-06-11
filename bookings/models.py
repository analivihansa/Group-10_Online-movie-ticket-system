from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    image_file_name = models.CharField(max_length=100, default='default.jpg')

    def __str__(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} at {self.date_time}"

class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(default='example@example.com')
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.showtime.movie.title}"







