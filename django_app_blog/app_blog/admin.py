from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Админка для создания рецептов
    """
    list_display = ('title', 'text', 'heading', 'cooking_time', 'get_image', 'serving', 'published_at', 'edited_at', 'views_count', 'slug', 'is_published')
    prepopulated_fields = {'slug': ('title', ), }
    list_editable = ('text', 'heading', 'cooking_time', 'serving', 'is_published')
    list_filter = ('cooking_time', 'published_at', 'edited_at')
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="150" height="100">')

    get_image.short_description = 'Фото'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Админка для создания комментариев
    """
    list_display = ('text', 'published_at', 'recipe', 'is_published')
    list_filter = ('published_at', )
    # list_editable = ('text', )
