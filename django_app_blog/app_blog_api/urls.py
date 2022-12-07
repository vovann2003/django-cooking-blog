from django.urls import path
from .api import RecipeAPIView, RecipeDetailAPIView, RecipePostAPIView


urlpatterns = [
    path('recipe/', RecipeAPIView.as_view(), name='recipe-api'),
    path('recipe/<int:pk>', RecipeDetailAPIView.as_view(), name='recipe-detail-api'),
    path('recipe-post/', RecipePostAPIView.as_view(), name='recipe-post-api'),
]
