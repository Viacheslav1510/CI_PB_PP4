from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField


class Tour(models.Model):
    tour_name = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=250, default='kerry tour')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    max_seats = models.IntegerField(default=50)
    tour_image = CloudinaryField(
        'tour_image',
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.tour_name}"


TIME_CHOICES = (
    ("8 AM", "8 AM"),
    ("10 AM", "10 AM"),
    ("12 PM", "12 PM"),
    ("14 PM", "14 PM"),
)

SEAT_CHOCES = (
    (1, "One Seat"),
    (2, "Two seats"),
    (3, "Three seats"),
    (4, "Four seats"),
    (5, "Four seats"),
    )


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phoneRegex = RegexValidator(
        regex=r'^\+?1?\d{8,15}$',
        message="Please enter a valid phone number,"
        "e.g. 123456789. Up to 15 digits allowed.",
        code="invalid"
    )
    phone = models.CharField(
        validators=[phoneRegex],
        max_length=16,
        null=True,
        blank=True
    )
    time = models.CharField(
        max_length=10,
        choices=TIME_CHOICES,
        default="8 PM"
    )
    tour_date = models.DateField()
    number_of_seats = models.CharField(
        max_length=10,
        choices=SEAT_CHOCES,
        default=1
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return f"Tour: {self.tour}, name: {self.name}," \
                f"date: {self.tour_date}, time: {self.time}"

    
