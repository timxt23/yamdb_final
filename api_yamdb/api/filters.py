import django_filters
from reviews.models import Category, Genre, Title


class TitleFilter(django_filters.FilterSet):
    """Фильтерсет для фильтрации по модели Title"""

    category = django_filters.ModelMultipleChoiceFilter(
        field_name='category__slug',
        to_field_name='slug',
        queryset=Category.objects.all()
    )
    genre = django_filters.ModelMultipleChoiceFilter(
        field_name='genre__slug',
        to_field_name='slug',
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Title
        fields = ['category', 'genre', 'name', 'year']
