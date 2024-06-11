from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Movie, Showtime, Booking

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration', 'image_file_name')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Showtime)
admin.site.register(Booking)

