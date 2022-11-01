from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from .models import catalog_category, catalog_item, catalog_tag


class StaticUrlTests(TestCase):
    args = {
        '': 200,
        '123/': 200,
        '65/': 200,
        'abc/': 404,
        'a.s71/': 404,
        '-149/': 404,
        '-pqoi/': 404,
        '12.751/': 404,
        '.112/': 404,
    }

    def test_catalog_endpoint(self):
        for i in self.args.keys():
            response = Client().get('/catalog/{}'.format(i))
            self.assertEqual(response.status_code, self.args[i])


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = (catalog_category.objects
                        .create(is_published=True,
                                name='Тестовая категория',
                                slug='test-category-slug',
                                weight=150))
        cls.tag = (catalog_tag.objects
                   .create(is_published=True,
                           name='Тестовый тэг',
                           slug='test-tag-slug'))
        cls.category.save()
        cls.tag.save()

    def test_unable_to_create_one_letter(self):
        item_count = catalog_item.objects.count()

        with self.assertRaises(ValidationError):
            self.item = catalog_item(name='Тестовый айтем',
                                     category=self.category,
                                     text='some txt 123.1 превос')
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        with self.assertRaises(ValidationError):
            self.item1 = catalog_item(name='Тестовый айтем1',
                                      category=self.category,
                                      text='Роскошн rfrbt askdnjq')
            self.item1.full_clean()
            self.item1.save()
            self.item1.tags.add(self.tag)

        self.assertEqual(catalog_item.objects.count(), item_count)

    def test_able_to_create_one_letter(self):
        item_count = catalog_item.objects.count()

        self.item = catalog_item(name='Тестовый айтем',
                                 category=self.category,
                                 text='Роскошно some words 109031')
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        self.item1 = catalog_item(name='Тестовый айтем1',
                                  category=self.category,
                                  text='какие-то слова..12 превосходно sfj,s')
        self.item1.full_clean()
        self.item1.save()
        self.item1.tags.add(self.tag)

        self.assertEqual(catalog_item.objects.count(), item_count + 2)
