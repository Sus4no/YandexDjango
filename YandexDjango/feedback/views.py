from django.shortcuts import render, redirect
from django.core.mail import send_mail
from feedback.forms import FeedbackForm
from feedback.models import Feedback


def feedback_page(request):
    template_name = 'feedback/index.html'
    form = FeedbackForm(request.POST or None)
    context = {
        'form': form
    }

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        Feedback.objects.create(
            text=text
        )
        send_mail(
            'Привет, пользователь',
            text,
            'from@example.com',
            ['to@example.com'],
            fail_silently=False
        )
        return redirect('feedback:feedback')

    return render(request, template_name, context)
