from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (Feedback.text.field.name, )
        labels = {
            Feedback.text.field.name: 'Текст'
        }
        help_texts = {
            Feedback.text.field.name: 'Написать текст здесь'
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
