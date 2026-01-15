from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from apps.dishes.models import Dish, DishIngredientGramm
import json


@require_POST
def find_dishes(request):
    data = json.loads(request.body)
    ingredient_slugs = data.get("ingredients", [])

    dishes = Dish.objects.filter(
        dishingredientgramm__dish_ingredient__slug__in=ingredient_slugs
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
