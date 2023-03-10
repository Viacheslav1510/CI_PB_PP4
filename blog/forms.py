from django import forms
from .models import PostModel, Comment


class PostModelForm(forms.ModelForm):
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
    class Meta:
        model = PostModel
        fields = ('title', 'excerpt', 'content', 'featured_image')
        widgets = {
            'excerpt': forms.Textarea(attrs={'rows': 4}),
            'content': forms.Textarea(attrs={'rows': 7}),
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
