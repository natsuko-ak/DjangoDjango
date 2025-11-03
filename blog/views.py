from django.shortcuts import render, get_object_or_404, redirect
from .models import Post  # <- Postモデルをインポート
from .forms import PostForm

def index(request):
    posts = Post.objects.all().order_by('-created_at')  # 投稿を新しい順に取得
    return render(request, 'blog/index.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # 投稿後に一覧ページへ戻る
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id) # 編集対象を取得

    if request.method == 'POST':
            form = PostForm(request.POST, instance=post) # ← 既存データで更新
            if form.is_valid():
                form.save()
                return redirect('index')
    else:
        form = PostForm(instance=post)  # ← 初期値を表示
        
    return render(request, 'blog/edit.html', {'form': form})