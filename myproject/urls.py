from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('post/<int:post_id>/', views.single_post, name='single_post'),
]
