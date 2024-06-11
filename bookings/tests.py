from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Showtime, Booking
from datetime import timedelta
from django.utils import timezone

class BookingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test user', password='test password')
        self.movie = Movie.objects.create(title='Test Movie', description='Test Description', duration=timedelta(hours=2))
        self.showtime = Showtime.objects.create(movie=self.movie, date_time=timezone.now())

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, 'Test Movie')

    def test_showtime_creation(self):
        self.assertEqual(self.showtime.movie, self.movie)

    def test_booking_creation(self):
        booking = Booking.objects.create(user=self.user, showtime=self.showtime, seats=2)
        self.assertEqual(booking.seats, 2)
        self.assertEqual(booking.user.username, 'test user')
        self.assertEqual(booking.showtime.movie.title, 'Test Movie')

