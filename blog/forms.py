# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import PostModel, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PostModelForm(forms.ModelForm):
    """
    A class to create form for Post Model
    """
    class Meta:
        model = PostModel
        fields = ('title', 'excerpt', 'content', 'featured_image')
        widgets = {
            'excerpt': forms.Textarea(attrs={'rows': 4}),
            'content': forms.Textarea(attrs={'rows': 7}),
            }

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        self.fields['featured_image'].required = True


class PostUpdateForm(forms.ModelForm):
    """
    A class to create form for updating post view
    """
    class Meta:
        model = PostModel
        fields = ('title', 'excerpt', 'content', 'featured_image')
        widgets = {
            'excerpt': forms.Textarea(attrs={'rows': 4}),
            'content': forms.Textarea(attrs={'rows': 7}),
            }

    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.fields['featured_image'].required = True


class CommentForm(forms.ModelForm):
    """
    A class to create form for Comment model
    """
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'Add comment here...',
            'rows': 2,
        })
    )

    class Meta:
        model = Comment
        fields = ('body',)
