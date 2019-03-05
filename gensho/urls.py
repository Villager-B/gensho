from django.urls import path
from . import views

app_name = 'gensho'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('comment/<int:post_pk>', views.CommentView.as_view(), name='comment'),
    path('comment-vote/<int:pk>', views.comment_vote, name='comment_vote'),
    path('post-vote/<int:pk>', views.post_vote, name='post_vote'),
    path('ranking/', views.RankingView.as_view(), name='ranking'),
    path('about/', views.AboutView.as_view(), name='about'),
]
