from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Category, Tag, Item


class StaticUrlTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.status_code, 200)


class TaskPagesTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = (Category.objects
                        .create(is_published=True,
                                name='Тестовая категория',
                                slug='test-category-slug',
                                weight=150))

        cls.tag = (Tag.objects
                   .create(is_published=True,
                           name='Тестовый тэг',
                           slug='test-tag-slug'))

        cls.item = Item(name='Тестовый айтем',
                        category=cls.category,
                        text='Роскошно some words 109031')

        cls.item2 = Item(name='Тестовый айтем2',
                         category=cls.category,
                         text='Роскошно some words')

        cls.category.save()
        cls.tag.save()
        cls.item.save()
        cls.item2.save()
        cls.item.tags.add(cls.tag)

    def test_home_page_show_correct(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
