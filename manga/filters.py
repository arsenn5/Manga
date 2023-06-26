from django_filters import rest_framework as filters

from manga.models import Manga

class Mangafilter(filters.FilterSet):
    type = filters.NumberFilter
    genre = filters.NumberFilter
    year = filters.RangeFilter()
    ru_name = filters.CharFilter
    eng_name = filters.CharFilter()

    class Meta:
        model = Manga
        fields = ['type', 'genre', 'year', 'eng_name', 'ru_name']
