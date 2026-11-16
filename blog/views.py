from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .forms import PostForm, CommentForm
from .models import Post, Category


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(Post, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.post = self.post_obj
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post_obj
        return context

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.post_obj.pk})

class CategoryListView(ListView):
    model = Category


class CategoryDetailView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def dispatch(self, request, *args, **kwargs):
        self.category = get_object_or_404(Category, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.category.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context