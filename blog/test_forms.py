from django.test import TestCase
from .forms import PostModelForm, PostUpdateForm, CommentForm


class TestPostModelForm(TestCase):
    """
    A class to test blog app post model form
    """
    def test_post_title_is_required(self):
        """
        Test to check required title field
        """
        form = PostModelForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test to check post model form fields existence
        """
        form = PostModelForm()
        self.assertEqual(
            form.Meta.fields,
            ('title', 'excerpt', 'content', 'featured_image'))


class TestPostUpdateForm(TestCase):
    """
    A class to test blog app post update form
    """
    def test_update_image_is_required(self):
        """
        Test to check required featured_image field
        """
        form = PostUpdateForm({'featured_image': ''})
        self.assertFalse(form.is_valid())


class TestCommentForm(TestCase):
    """
    A class to test blog app comment form
    """
    def test_body_field_is_required(self):
        """
        Test to check required body field
        """
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
