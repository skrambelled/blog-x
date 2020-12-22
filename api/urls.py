from django.urls import path
from .views import PostAPIListCreateView, PostAPIDetailUpdateView, PostAPIDetailDeleteView

urlpatterns = [
    path('create/', PostAPIListCreateView.as_view(), name='api/v1/create'),
    path('update/<int:pk>', PostAPIDetailUpdateView.as_view(), name='api/v1/update'),
    path('delete/<int:pk>', PostAPIDetailDeleteView.as_view(), name='api/v1/delete')
]