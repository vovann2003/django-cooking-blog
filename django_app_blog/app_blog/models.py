from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    """
    Модель Профиль пользователя
    """
    first_name = models.CharField(max_length=56, verbose_name='имя')
    last_name = models.CharField(max_length=56, verbose_name='фамилия')
    email = models.EmailField(blank=True, null=True, verbose_name='электронная почта', unique=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, blank=True, null=True, verbose_name='никнейм', unique=True)
    photo = models.ImageField(upload_to='media/images/profile/', verbose_name='фото пользователя', null=True, blank=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'profile'
        verbose_name_plural = 'profile'


class Recipe(models.Model):
    """
    Модель Рецепт
    """

    SNACK = 'SN'
    FIRST_COURSE = 'FC'
    SECOND_COURSE = 'SC'
    BAKING = 'BK'
    MARINADE = 'MR'
    POTABLES = 'PT'
    SEASONING = 'SS'
    DESSERT = 'DT'
    SAUCE = 'SC'

    HEADING = (
        (SNACK, 'Закуска'),
        (FIRST_COURSE, 'Первое блюдо'),
        (SECOND_COURSE, 'Второе блюдо'),
        (BAKING, 'Выпечка'),
        (MARINADE, 'Маринад'),
        (POTABLES, 'Напитки'),
        (SEASONING, 'Приправа'),
        (DESSERT, 'Десерт'),
        (SAUCE, 'Соус'),
    )

    title = models.CharField(max_length=160, verbose_name='название блюда')
    text = models.TextField(verbose_name='текст')
    heading = models.CharField(choices=HEADING, max_length=2, verbose_name='рубрика')
    cooking_time = models.FloatField(verbose_name='время приготовления', blank=True, null=True)
    photo = models.ImageField(verbose_name='фото блюда', upload_to='media/%Y/%m/%d')
    serving = models.IntegerField(verbose_name='порции')
    published_at = models.DateField(auto_now_add=True, verbose_name='опубликовано')
    edited_at = models.DateField(auto_now=True, verbose_name='изменено')
    views_count = models.PositiveIntegerField(default=0, verbose_name='кол-во просмотров')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='слаг', default=None)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'recipe_slug': self.slug})

    class Meta:
        db_table = 'recipe'
        ordering = ('-published_at', )
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'


class RecipeCountViews(models.Model):
    session_id = models.CharField(max_length=150, db_index=True)
    recipe_id = models.ForeignKey(Recipe, blank=True, null=True, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.session_id


class Comment(models.Model):
    """
    Класс Комментарий
    """
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(max_length=1500, verbose_name='комментарий')
    published_at = models.DateField(auto_now_add=True, verbose_name='опубликовано')
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, blank=True, null=True, related_name='comment_recipe')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
