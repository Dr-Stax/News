from django.shortcuts import render
from django.views.generic import  DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .models import Articles
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Comments
from .forms import CommentForm
from django.urls import reverse
# Create your views here.


class ArticleListView(LoginRequiredMixin, ListView):
    model = Articles
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'

class ArticlesDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'articles/article_detail.html'

class CreateArticle(LoginRequiredMixin, CreateView):
    model = Articles
    template_name = 'articles/create_view.html'
    fields = [
        'title',
        'body',
    ]

    success_url = reverse_lazy("article_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ArticleUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    model = Articles
    template_name = 'articles/update_news.html'
    fields = ['title', 'body',]
    success_url = reverse_lazy('article_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class DeleteBlogPost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    model = Articles
    template_name = 'articles/delete_post.html'
    success_url = reverse_lazy('article_list')


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = CommentForm
    template_name = "articles/comment.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Articles.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articles_detail', kwargs={'pk': self.kwargs['pk']})
