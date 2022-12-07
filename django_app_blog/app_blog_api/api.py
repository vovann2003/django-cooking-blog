from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework.backends import DjangoFilterBackend
from .filters import RecipeFilter
from .serializers import RecipeSerializer
from app_blog.models import Recipe


class RecipeAPIView(ListAPIView):
    """
    API для просмотра всех рецептов на сайте. Может просматривать каждый пользователь
    """
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.filter(is_published=True)
    permission_classes = (AllowAny, )
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = RecipeFilter

    @swagger_auto_schema(
        operation_summary='All recipes list',
        operation_description='This endpoint shows all recipes info',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RecipeDetailAPIView(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericAPIView):
    """
    API для детального просмотра, изменения или удаления рецепта. Доступно только для суперпользователя
    """
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.filter(is_published=True)
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(
        operation_summary='Recipe info',
        operation_description='This endpoint shows recipe info',
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Recipe editing',
        operation_description='This endpoint edit recipe',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Recipe deleting',
        operation_description='This endpoint delete recipe'
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RecipePostAPIView(mixins.CreateModelMixin,
                        GenericAPIView):
    """
    API для добавления нового рецепта. Доступно только для суперпользователя
    """
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.filter(is_published=True)
    permission_classes = (IsAdminUser, )

    @swagger_auto_schema(
        operation_summary='Post recipes',
        operation_description='This endpoint load recipe into the database',
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
