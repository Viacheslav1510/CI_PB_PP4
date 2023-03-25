# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from daterangefilter.filters import DateRangeFilter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import ContactModel
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    """
    A clas to register Contact Model in admin panel,
    display fields and provide serach on field
    """
    list_filter = (
        'first_name',
        'last_name',
        'email',
        ('created_date', DateRangeFilter),
        )
    list_display = (
        'user',
        'first_name',
        'last_name',
        'email',
        'message',
        'created_date')

    search_fields = ['user__username', 'last_name', 'last_name',]
