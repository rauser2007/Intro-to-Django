from django.urls import path
from . import views

urlpatterns = [
    # Список всіх постів
    path('posts/', views.post_list, name='post_list'),
    
    # Детальна сторінка конкретного посту
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    
    # Пости за автором
    path('author/<int:author_id>/posts/', views.posts_by_author, name='posts_by_author'),
]
