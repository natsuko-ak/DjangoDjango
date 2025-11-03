from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 記事一覧
    path('<int:pk>/', views.detail, name='detail'), # 記事詳細
    path('create/', views.create, name='create'), # 新規記事作成
    path('<int:post_id>/edit/',views.edit, name='edit'), #
]
