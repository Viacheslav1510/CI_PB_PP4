from django.test import TestCase
import tempfile
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from .models import PostModel
from .forms import PostModelForm
from django.core.files.uploadedfile import SimpleUploadedFile


class TestBlogViews(TestCase):

    def setUp(self):
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
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_post_detail_page(self):
        slug = self.post.slug
        response = self.client.get(reverse('blog-detail', args=[slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog-details.html')

    def test_get_create_post_page(self):
        response = self.client.get('/new-post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add-blog.html')

    def test_get_post_edit_page(self):
        slug = self.post.slug
        response = self.client.get(reverse('blog-edit', args=[slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit-blog.html')

    def test_get_post_delete_page(self):
        slug = self.post.slug
        response = self.client.get(reverse('blog-delete', args=[slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/delete-blog.html')

    def test_user_can_create_post(self):
        """
        Test to create post
        """
        self.client.login(username='albajessica', password='bartolito')
        response = self.client.post(
            '/new-post/',
            {
                'title': "Test Create",
                'content': 'test',
                'excerpt': 'test',
                'author': self.user,
                'featured_image': tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
        )
        print(response)
        self.assertRedirects(response, '/blog/')

    def test_form_creation_is_valid(self):
        # self.client.login(username='albajessica', password='bartolito')
        image_path = 'static/images/man-1.jpg'
        form_data = {
            'title': "Test Creation",
            'content': 'test',
            'excerpt': 'test',
            'author': self.user,
            'featured_image': 'image'
        }
       
        form = PostModelForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())
