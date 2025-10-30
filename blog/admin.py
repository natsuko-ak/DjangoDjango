from django.contrib import admin

# Register your models here.
from .models import Post # <- models.pyからPostをインポート

admin.site.register(Post)  # <- Postモデルを管理画面に登録
