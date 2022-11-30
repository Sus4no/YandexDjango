from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse

from feedback.forms import FeedbackForm
from feedback.models import Feedback


def feedback_page(request):
    template_name = 'feedback/index.html'
    form = FeedbackForm(request.POST or None)
    context = {
        'form': form,
        'sent': request.GET.get('sent', False)
    }

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        Feedback.objects.create(
            text=text
        )
        send_mail(
            'Привет, пользователь',
            text,
            settings.SENDER_MAIL,
            [settings.RECEIVER_MAIL],
            fail_silently=False
        )
        return redirect(f'{reverse("feedback:feedback")}?sent=True')

    return render(request, template_name, context)
