from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from .serializers import PostSerializer
from blog.models import Post

class PostAPIListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIDetailUpdateView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIDetailDeleteView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer