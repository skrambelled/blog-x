from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class HomePageView(ListView):
    template_name = 'blog/home.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post


class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    model = Post
    fields = ['title', 'author', 'body']
    

class PostUpdateView(UpdateView):
    permission_classes = (IsAuthorOrReadOnly,)
    template_name = 'blog/post_update.html'
    model = Post
    fields = ['title', 'body']


class PostDeleteView(DeleteView):
    permission_classes = (IsAuthorOrReadOnly,)
    template_name = 'blog/post_delete.html'
    model = Post
    success_url = reverse_lazy('blog/home')
