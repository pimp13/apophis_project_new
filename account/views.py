import datetime
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views import View
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .models import User

from account.forms import RegisterForm, LoginForm

class RegisterView(View):
    def get(self, request: HttpRequest):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'account/register.html', context)

    def post(self, request: HttpRequest):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user: bool = User.objects.filter(email__iexact=email).exists()
            if user:
                form.add_error('email', 'ایمیل وارد شده تکراری میباشد')
            else:
                # login(request, user)
                User.objects.create_user(
                    email=email,
                    password=password,
                    username=username,
                    email_active_code=get_random_string(120)
                )
                return redirect(reverse('home'))
        context = {
            'form': form
        }
        return render(request, 'account/register.html', context)

class LoginView(View):
    def get(self, request: HttpRequest):
        form: LoginForm = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'account/login.html', context)

    def post(self, request: HttpRequest):
        form: LoginForm = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user: User = User.objects.filter(username__iexact=username).first()
            if user is not None:
                is_match = user.check_password(password)
                if user.is_active and is_match:
                    user_auth = authenticate(self.request, username=username, password=password)
                    if user_auth is not None:
                        login(request, user)
                        user.last_login = datetime.datetime.now()
                        user.save()
                        return redirect(reverse('home'))
                else:
                    form.add_error('password', 'نام کاربری یا کلمه عبور صحیح نمی باشد')
            else:
                form.add_error('password', 'کاربری با این یوزرنیم وجود ندارد')
        context = {
            'form': form
        }
        return render(request, 'account/login.html', context)

class ActiveAccountView(View):
    def get(self, request, token):
        user: User = User.objects.filter(email_active_code__iexact=token).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(120)
                user.save()
                # todo: show success message
                return redirect(reverse('login'))
            else:
                # todo: show message
                return redirect(reverse('home'))
        raise Http404
