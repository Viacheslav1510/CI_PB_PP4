from django.test import TestCase
from .forms import PostModelForm, PostUpdateForm, CommentForm


class TestPostModelForm(TestCase):

    def test_post_title_is_required(self):
        form = PostModelForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = PostModelForm()
        self.assertEqual(
            form.Meta.fields,
            ('title', 'excerpt', 'content', 'featured_image'))