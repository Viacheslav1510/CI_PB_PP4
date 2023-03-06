from django import forms
from .models import PostModel, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'excerpt', 'content', 'featured_image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
