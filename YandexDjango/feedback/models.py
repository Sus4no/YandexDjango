from django.db import models


class Feedback(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.created_on)

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'
