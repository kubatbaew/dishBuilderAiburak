from django.urls import path

from apps.dishes import views as dish_views
from apps.dishes import api_views as dish_api


urlpatterns = [
    path('', dish_views.homepage, name="homepage"),
    path('ingredients/', dish_views.ingredients, name="ingredients"),
    path('dishes/', dish_views.list_dishes, name="list_dishes"),

    path('login/', dish_views.login, name="login"),
    path('sign_up/', dish_views.sign_up, name="sign_up"),
    path('logout_logics/', dish_views.logout_logics, name="logout_logics"),
    
    path("api/find-dishes/", dish_api.find_dishes, name="find_dishes"),
]
