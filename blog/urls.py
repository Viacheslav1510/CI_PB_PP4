from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_home, name='blog'),
    path('<str:slug>', views.blog_detail, name="blog-detail")
]