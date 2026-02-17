from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from apps.dishes.models import Dish, DishIngredientGramm, Favorite, FavoriteItems
import json

from django.shortcuts import get_object_or_404


@require_POST
def find_dishes(request):
    data = json.loads(request.body)
    ingredient_slugs = data.get("ingredients", [])

    dishes = Dish.objects.filter(
        ingredients_gramms__dish_ingredient__slug__in=ingredient_slugs
    ).distinct()

    result = []

    for dish in dishes:
        result.append({
            "id": dish.id,
            "name": dish.title,
            "desc": dish.description,
            "image": dish.image.url if dish.image else "",
        })

    return JsonResponse({"dishes": result})


def calculator_logics(request):
    dish_id = request.GET.get("dish_id")
    grams = float(request.GET.get("grams"))

    dish = get_object_or_404(Dish, id=dish_id)

    base_grams = 1  # на сколько грамм заданы ингредиенты
    coef = base_grams * grams
    print(coef)

    result = []

    for item in dish.ingredients_gramms.select_related("dish_ingredient"):
        result.append({
            "ingredient": item.dish_ingredient.title,
            "grams": round(item.gramm * coef)
        })

    return JsonResponse({
        "dish": dish.title,
        "ingredients": result
    })


def save_to_favorite(request):
    if request.method == "POST":
        data = json.loads(request.body)
        dish_id = data.get('dish_id')
        ingredients = data.get('ingredients')
        
        print(dish_id)
        print(ingredients)

        dish = Dish.objects.get(id=dish_id)

        user_favorite = Favorite.objects.create(
            user=request.user,
            dish=dish,
        )
        items = [
            FavoriteItems(
                favorite=user_favorite,
                title=item["title"],
                gramm=item["grams"]
            )
            for item in ingredients
        ]
        FavoriteItems.objects.bulk_create(items)

        return JsonResponse({'status': 'ok'})
