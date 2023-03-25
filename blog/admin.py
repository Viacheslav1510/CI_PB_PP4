# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from daterangefilter.filters import DateRangeFilter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import PostModel, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(PostModel)
class PostModelAdmin(SummernoteModelAdmin):
    """
    A class to register post model in admin panel
    """
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = (
        'title',
        'author__username',
        ('date_created', DateRangeFilter),
        )
    list_display = ('title', 'author', 'date_created')
    search_fields = ['title', 'author__username']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    A class to register comment model in admin panel
    """
    list_display = ('user', 'post', 'body', 'date_created', 'approved')
    list_filter = (
        'user__username',
        'approved',
        ('date_created', DateRangeFilter),
        )
    search_fields = ('user__username', 'body', 'post')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
