from django.db import models
from django.utils.safestring import mark_safe
from django.http import Http404
from Core.models import Core
from Core.validators import validate_if_words_there
from sorl.thumbnail import get_thumbnail
from tinymce.models import HTMLField


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


class ItemManager(models.Manager):
    def on_homepage(self):
        return (
            self.get_queryset()
            .filter(is_published=True, is_on_main=True)
            .select_related('category')
            .prefetch_related(
                models.Prefetch(
                    'tags',
                    queryset=Tag.objects.filter(is_published=True).only('name')
                ))
            .order_by('name')
            )

    def on_item_list(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .select_related('category')
            .prefetch_related(
                models.Prefetch(
                    'tags',
                    queryset=Tag.objects.filter(is_published=True).only('name')
                ))
            .order_by('category__name')
            )

    def on_item_detail(self, pk):
        values = (
            self.get_queryset()
            .filter(id=pk, is_published=True)
            .select_related('category')
            .prefetch_related(
                models.Prefetch(
                    'tags',
                    queryset=Tag.objects.filter(is_published=True).only('name')
                )))
        if values:
            return values
        raise Http404


class Item(Core):
    objects = ItemManager()

    is_on_main = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    text = HTMLField(validators=[validate_if_words_there('превосходно',
                                                         'роскошно')],
                     help_text='Описание должно быть больше 2х слов' +
                               ' и содержать слова ' +
                               '\"превосходно, роскошно\"', )

    upload = models.ImageField(upload_to='uploads/%Y/%m', blank=True)
    # gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '400x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">')
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'


class Gallery(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/%Y/%m/')

    @property
    def get_img(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}">')
        return 'Нет изображения'

    image_tmb.short_description = 'Изображение'
    image_tmb.allow_tags = True

    def __str__(self):
        return f'Изображение {self.item.name}'

    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'
