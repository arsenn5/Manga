from django.urls import path

from test_movie.views import MangaView, MangaDetailView
from . import views

urlpatterns = [
    path('manga', MangaView.as_view({
        'get': 'list',
    })),
    path('manga/<int:id>', MangaDetailView.as_view({
        'get': 'retrieve',
    })),
    path('comment/', views.CommentView.as_view({
        'get': 'list',
        'post': 'create',
    })),
]
