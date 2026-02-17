from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User

from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404

from apps.dishes.models import DishIngredient, Dish, Favorite


@login_required(login_url="login")
def homepage(request):
    return render(request, "index.html", locals())


@login_required(login_url="login")
def ingredients(request):
    ingredients_obj = DishIngredient.objects.all()
    
    return render(request, "ingredients.html", locals())


@login_required(login_url="login")
def list_dishes(request):
    dishes = Dish.objects.all()

    return render(request, "dishes.html", locals())


@login_required(login_url="login")
def favorite(request):
    favorites = Favorite.objects.filter(user=request.user)[::-1]

    return render(request, "favorite.html", locals())

@login_required(login_url="login")
def delete_favorite(request, pk):
    favorite = get_object_or_404(
        Favorite,
        id=pk,
        user=request.user
    )
    favorite.delete()
    
    return redirect('favorite')


@login_required(login_url="login")
def detail_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)

    return render(request, "dish-detail.html", locals())


@login_required(login_url="login")
def calculator(request):
    dishes = Dish.objects.all()

    return render(request, "calculator.html", locals())


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
