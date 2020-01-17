from django.shortcuts import render
from .models import Post  # kropka oznacza biezacy katalog lub aplikacja znajduje sie w tym samym katalogu
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #zmienna dla QuerySeru.
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # commit sygnalizuje ze jeszcze nie chcemy zapisywac modelu Post, najpierw trzeba dodac autora
            post.author = request.user
            post.published_date = timezone.now()
            post.save()  # zachowuje zmiany
            return redirect('post_detail', pk=post.pk) # to mowi: przejdz na strone post_detail, zeby zobaczyc nowo utworzony wpis
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})