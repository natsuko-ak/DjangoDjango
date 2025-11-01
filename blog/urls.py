from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 記事一覧
    path('<int:pk>/', views.detail, name='detail'), # 記事詳細
]
