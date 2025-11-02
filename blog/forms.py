from django import forms
from .models import Post

class PostForm(forms.ModelForm): # models.pyで作ったPostモデルを元に自動でフォーム生成してくれるクラス。
    class Meta:
        model = Post
        fields = ['title', 'content']