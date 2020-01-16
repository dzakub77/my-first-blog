from django.shortcuts import render
from .models import Post  # kropka oznacza biezacy katalog lub aplikacja znajduje sie w tym samym katalogu
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #zmienna dla QuerySeru.
    return render(request, 'blog/post_list.html', {'posts': posts})
