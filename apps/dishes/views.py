from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User

from django.contrib import messages

from django.shortcuts import render, redirect

from apps.dishes.models import DishIngredient


@login_required(login_url="login")
def homepage(request):
    return render(request, "index.html", locals())


@login_required(login_url="login")
def ingredients(request):
    ingredients_obj = DishIngredient.objects.all()
    
    return render(request, "ingredients.html", locals())


def login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("homepage")
        else:
            messages.error(request, "Неверный логин или пароль")

    return render(request, "login.html", locals())


def sign_up(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Пользователь с таким логином уже существует")
        else:
            User.objects.create_user(
                username=username,
                password=password
            )
            return redirect("homepage")

    return render(request, "sign-up.html", locals())


def logout_logics(request):
    logout(request)
    return redirect('login')
