from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) # 記事タイトル
    content = models.TextField()             # 記事本文
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時

    def __str__(self):
        return self.title