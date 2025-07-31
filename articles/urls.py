from django.urls import path, include
from.views import ArticleListView, ArticlesDetailView, CreateArticle, ArticleUpdate, DeleteBlogPost, AddCommentView

urlpatterns = [
    path("", ArticleListView.as_view(), name='article_list'),
    path("<int:pk>", ArticlesDetailView.as_view(), name='articles_detail'),
    path("new/", CreateArticle.as_view(), name="article_new"),
    path("article/<int:pk>/edit", ArticleUpdate.as_view(), name="edit"),
    path("article/<int:pk>/delete", DeleteBlogPost.as_view(), name='delete_post'),
    path("comment/<int:pk>/", AddCommentView.as_view(), name='add_comment'),


    
]