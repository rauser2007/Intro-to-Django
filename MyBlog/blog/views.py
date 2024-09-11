from django.shortcuts import render
from .models import Post, Author  # Замініть на відповідну модель, яка містить ваші пости

def post_list(request):
    posts = Post.objects.all()  # Отримуємо всі пости з бази даних
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def posts_by_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author)

    return render(request, 'blog/posts_by_author.html', {'author': author, 'posts': posts})