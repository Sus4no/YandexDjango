from django.db import models
from .validators import validate_if_words_there


class Core(models.Model):
    is_published = models.BooleanField(default=True)
    name = models.CharField(max_length=150, help_text='max 150 символов')

    class Meta:
        abstract = True


class catalog_tag(Core):
    slug = models.TextField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'


class catalog_category(Core):
    slug = models.SlugField(max_length=200, unique=True)
    weight = models.PositiveSmallIntegerField(default=100)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class catalog_item(Core):
    category = models.ForeignKey(catalog_category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(catalog_tag)
    text = models.TextField(validators=[validate_if_words_there, ],
                            help_text='Описание должно быть больше 2х слов' +
                                      ' и содержать слова ' +
                                      '\"превосходно, роскошно\"')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
