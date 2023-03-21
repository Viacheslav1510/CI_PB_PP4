from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_home, name='blog'),
    path('new-post/', views.create_post, name='add-blog'),
    path('<str:slug>', views.post_details, name='blog-detail'),
    path('post-edit/<str:slug>/', views.edit_post, name='blog-edit'),
    path('post-delete/<str:slug>/', views.delete_post, name='blog-delete'),
]
