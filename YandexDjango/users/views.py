from django.shortcuts import render, redirect
from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignUpForm, ProfileForm


def signup(request):
    template_name = 'users/signup.html'
    form = SignUpForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        if password == confirm_password:
            get_user_model().objects.create(
                email=email,
                password=password,
                is_superuser=False,
            )
            return redirect(reverse('users:login'))
    return render(request, template_name, context)


def user_list(request):
    template_name = 'users/user_list.html'
    users = get_user_model().objects.filter(is_active=True).all()
    context = {
        'users': users
    }
    return render(request, template_name, context)


def user_detail(request, id):
    template_name = 'users/user_detail.html'
    user = get_user_model().objects.get(pk=id)
    context = {
        'user': user
    }
    return render(request, template_name, context)


@login_required
def profile(request):
    template_name = 'users/user_profile.html'
    form = ProfileForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        birthday = form.cleaned_data['birthday']
        (get_user_model().objects.filter(id=get_user(request).id)
         .update(email=email, first_name=first_name, birthday=birthday))
        return redirect(reverse('homepage:home'))
    return render(request, template_name, context)
