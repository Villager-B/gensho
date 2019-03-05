from django.views import generic
from .models import Post, Comment
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from .forms import CommentCreateForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


class IndexView(generic.ListView):
    model = Post
    template_name = 'gensho/post_list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')  #inputのname
        if keyword:
            queryset = queryset.filter(
                Q(pk__icontains=keyword) | Q(text__icontains=keyword))

        return queryset


def comment_vote(request, pk):
    comments = get_object_or_404(Comment, pk=pk)
    comments.vote_star += 1
    comments.save()
    return redirect(request.META['HTTP_REFERER'])
    #return HttpResponseRedirect(reverse('gensho:detail', args=(Post.pk, )))


def post_vote(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    posts.star += 1
    posts.save()
    return redirect(request.META['HTTP_REFERER'])
    #return HttpResponseRedirect(reverse('gensho:detail', args=(Post.pk, )))


class DetailView(generic.DetailView):
    template_name = 'gensho/post_detail.html'
    model = Post


class CommentView(generic.CreateView):
    template_name = 'gensho/comment_form.html'
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('gensho:detail', pk=post_pk)


class RankingView(generic.ListView):
    model = Post
    template_name = 'gensho/ranking_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.order_by('-star')
        return queryset


class AboutView(generic.TemplateView):
    template_name = 'gensho/about.html'
