from rest_framework import serializers
from app_blog.models import Recipe, Comment


class RecipeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для рецептов
    """

    class Meta:
        model = Recipe
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для комментариев
    """

    class Meta:
        model = Comment
        fields = '__all__'
