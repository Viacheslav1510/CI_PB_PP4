# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Tour(models.Model):
    """
    A class to create Tour model
    """
    tour_name = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=500, default='kerry tour')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    max_seats = models.IntegerField(default=15)
    tour_image = CloudinaryField(
        'tour_image',
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.tour_name}"


class Booking(models.Model):
    """
    A class to create Booking model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phoneRegex = RegexValidator(
        regex=r'^(\+\d{1,3})?,?\s?\d{8,13}$',
        message="Please enter a valid phone number,"
        "e.g. +123456789. Up to 13 digits allowed.",
        code="invalid"
    )
    phone = models.CharField(
        validators=[phoneRegex],
        max_length=16,
        null=True,
        blank=True
    )
    tour_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return f"Tour: {self.tour}, name: {self.name}, " \
                f"date: {self.tour_date}"
