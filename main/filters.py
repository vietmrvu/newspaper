import django_filters
from .models import *
from django_filters import CharFilter


class ArticleSeriesFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = ArticleSeries
        fields = ['title']

class ArticleFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['title']