from django.shortcuts import render
from .models import Post  # <- Postモデルをインポート

def index(request):
    posts = Post.objects.all().order_by('-created_at')  # 投稿を新しい順に取得
    return render(request, 'blog/index.html', {'posts': posts})
