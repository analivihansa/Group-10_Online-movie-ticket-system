
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Showtime, Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_protect


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def showtime_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    showtimes = Showtime.objects.filter(movie=movie)
    return render(request, 'bookings/showtime_list.html', {'movie': movie, 'showtimes': showtimes})

@login_required
def book_ticket(request, showtime_id):
    showtime = get_object_or_404(Showtime, id=showtime_id)
    movie = showtime.movie  # Get the movie from the showtime
    if request.method == 'POST':
        seats = int(request.POST.get('seats', 1))
        selected_seats = request.POST.get('selected_seats', '')
        booking = Booking.objects.create(name=request.user.username, showtime=showtime, seats=seats)
        # Optionally save the selected seats if your Booking model supports it
        booking.selected_seats = selected_seats
        booking.save()
        return render(request, 'bookings/booking_confirmation.html', {'booking': booking, 'selected_seats': selected_seats})
    return render(request, 'bookings/book_ticket.html', {'showtime': showtime, 'movie': movie})



@csrf_protect
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'bookings/add_movie.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'bookings/register.html', {'form': form})
