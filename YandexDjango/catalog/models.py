from django.db import models
from Core.models import Core
from Core.validators import validate_if_words_there


class Tag(Core):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'


class Category(Core):
    slug = models.SlugField(max_length=200, unique=True)
    weight = models.PositiveSmallIntegerField(default=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Item(Core):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    text = models.TextField(validators=[validate_if_words_there('превосходно',
                                                                'роскошно')],
                            help_text='Описание должно быть больше 2х слов' +
                                      ' и содержать слова ' +
                                      '\"превосходно, роскошно\"')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
