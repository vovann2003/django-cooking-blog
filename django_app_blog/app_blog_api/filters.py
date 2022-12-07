from django_filters import rest_framework as filters
from app_blog.models import Recipe


class RecipeFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    cooking_time = filters.NumberFilter(field_name='cooking_time', lookup_expr='gte')
    serving = filters.NumberFilter(field_name='serving', lookup_expr='gte')
    published_at_from = filters.DateTimeFilter(field_name='published_at', lookup_expr='gte')
    published_at_to = filters.DateTimeFilter(field_name='published_at', lookup_expr='lte')
    views_count_more = filters.NumberFilter(field_name='views_count', lookup_expr='gte')
    views_count_less = filters.NumberFilter(field_name='views_count', lookup_expr='lte')

    class Meta:
        model = Recipe
        fields = (
            'title',
            'cooking_time',
            'serving',
            'published_at_from',
            'published_at_to',
            'views_count_more',
            'views_count_less',
        )
