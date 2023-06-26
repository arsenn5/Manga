from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from test_movie.filters import Mangafilter
from .models import Manga, Comment
from .serializers import MangaSerializer, MangaDetailSerializer, CommentCreateSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000


class MangaView(ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = Mangafilter
    pagination_class = LargeResultsSetPagination


class MangaDetailView(ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaDetailSerializer
    lookup_field = 'id'


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True)
    def edit(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = CommentCreateSerializer(comment)
        return Response(serializer.data)