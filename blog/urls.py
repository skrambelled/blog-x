from django.urls import path
from .views import HomePageView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='blog/home'),
    path('details/<int:pk>/', PostDetailView.as_view(), name='blog/post_detail'),
    path('new', PostCreateView.as_view(), name="blog/post_create"),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name="blog/post_update"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="blog/post_delete")
]
