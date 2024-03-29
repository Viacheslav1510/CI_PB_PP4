# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Comment, PostModel
from .admin import CommentAdmin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Test_Admin_Comment_Model(TestCase):
    """
    A class to test admin models
    """
    def setUp(self):
        """
        A function to create user, post and comment for testing
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
        self.site = AdminSite()
        self.commentModelAdmin = CommentAdmin(Comment,  self.site)

    def test_admin_can_approve_comments(self):
        """
        Test to approve comments in admin panel
        """
        comment = self.comment
        queryset = Comment.objects.filter(body='Test comment body')
        self.commentModelAdmin.approve_comments(comment, queryset)
        self.assertTrue(Comment.objects.get(body='Test comment body').approved)
