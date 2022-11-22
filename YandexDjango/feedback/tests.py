from django.test import TestCase, Client
from django.urls import reverse
from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm(None)

    def test_is_in_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertTrue(response.context['form'])

    def test_name_label(self):
        name_label = self.form.fields['text'].label
        self.assertEquals(name_label, 'Текст')

    def test_name_help_text(self):
        name_help_text = self.form.fields['text'].help_text
        self.assertEquals(name_help_text, 'Написать текст здесь')

    def test_create_task(self):
        obj_count = Feedback.objects.count()
        form_data = {
            'text': 'some text'
        }

        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True
        )

        self.assertRedirects(response, reverse('feedback:feedback'))

        self.assertEqual(Feedback.objects.count(), obj_count + 1)

        self.assertTrue(
            Feedback.objects.filter(
                text='some text',
                ).exists()
        )
