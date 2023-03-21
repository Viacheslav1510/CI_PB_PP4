from django.test import TestCase
import tempfile
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm


class TestBlogViews(TestCase):
    """
    A class for testing blog views
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
            content='test',
            excerpt='test',
            author=self.user,
            featured_image=tempfile.NamedTemporaryFile(suffix=".jpg").name)
        self.post.save()

    def test_get_blog_home_page(self):
        """
        Test to get blog home page
        """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_post_detail_page(self):
        """
        Test to get post details page
        """
        slug = self.post.slug
        response = self.client.get(reverse('blog-detail', args=[slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog-details.html')

    def test_get_create_post_page(self):
        """
        Test to get create post page
        """
        response = self.client.get('/new-post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add-blog.html')

    def test_get_post_edit_page(self):
        """
        Test to get edit post page
        """
        slug = self.post.slug
        response = self.client.get(reverse('blog-edit', args=[slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit-blog.html')

    def test_get_post_delete_page(self):
        """
        Test to get delete confirmation page
        """
        slug = self.post.slug
        response = self.client.get(reverse('blog-delete', args=[slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/delete-blog.html')

    def test_user_can_create_post(self):
        """
        Test to create post and redirect to 'blog' page
        """
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        response = self.client.post(
            '/new-post/',
            {
                'title': "Test Create",
                'content': 'test',
                'excerpt': 'test',
                'author': self.user,
                'featured_image': image
            }
        )
        self.assertRedirects(response, '/blog/')

    def test_form_creation_is_valid(self):
        """
        Test for PostModelForm validation
        """
        image_path = 'static/images/man-1.jpg'
        form_data = {
            'title': "Test Creation",
            'content': 'test',
            'excerpt': 'test',
            'author': self.user,
            'featured_image': 'image'
        }

        form = PostModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_can_edit_post(self):
        """
        Test to edit post
        """
        slug = self.post.slug
        response = self.client.post(
            reverse('blog-edit', args=[slug]), {
                        'title': "Edited Post Test",
                        'content': 'test',
                        'excerpt': 'test',
                        'slug': self.post.slug,
                        'author': self.user,
                        'featured_image': 'image'
                    })
        self.assertEquals(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEquals(self.post.title, 'Edited Post Test')

    def test_can_delete_post(self):
        """
        Test to delete post
        """
        slug = self.post.slug
        response = self.client.post(reverse('blog-delete',
                                    args=[slug]))
        self.assertRedirects(response, reverse('blog'), status_code=302)

    def test_can_comment(self):
        """
        Test for comment functionality
        """
        slug = self.post.slug
        response = self.client.post(
            reverse('blog-detail', args=[slug]), {
                'body': 'test comment'
            })
        self.assertEquals(response.status_code, 302)
