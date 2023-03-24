from django.contrib import admin
from .models import PostModel, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(PostModel)
class PostModelAdmin(SummernoteModelAdmin):
    """
    A class to register post model in admin panel
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date_created')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    A class to register comment model in admin panel
    """
    list_display = ('user', 'post', 'body', 'date_created', 'approved')
    list_filter = ('approved', 'date_created')
    search_fields = ('user', 'body', 'post')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
