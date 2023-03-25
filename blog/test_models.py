# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import PostModel, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestModels(TestCase):
    """
    A clas for testing blog app models
    """
    def setUp(self):
        """
        SetUp function to create user, login and create post
        """
        self.user = User.objects.create_user(
                username='albajessica', email='foo@gmail.com',
                password='bartolito')
        self.user.save()
        self.client.login(username='albajessica', password='bartolito')
        self.post = PostModel.objects.create(
            title="this is a test blog",
            author=self.user,
            )
        self.post.save()
        self.comment = Comment.objects.create(
            user=self.user,
            post=self.post,
            body='Test comment body'
        )
        self.comment.save()

    def test_post_string_method_returns_title(self):
        """
        Test to check string method for Post Model
        """
        post = self.post
        self.assertEqual(str(post), 'this is a test blog')

    def test_comment_string_method_returns_right_string(self):
        """
        Test to check string method for Comment model
        """
        comment = self.comment
        self.assertEqual(
            str(comment),
            f'Comment {comment.body} by {self.user.username}'
        )
