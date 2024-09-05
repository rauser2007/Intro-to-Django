from django.shortcuts import render
from .models import Post  # Замініть на відповідну модель, яка містить ваші пости

def post_list(request):
    posts = Post.objects.all()  # Отримуємо всі пости з бази даних
    return render(request, 'post_list.html', {'posts': posts})
