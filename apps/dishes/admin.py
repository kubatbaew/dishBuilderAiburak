from django.contrib import admin

from apps.dishes.models import Dish, DishIngredient, DishIngredientGramm


class DishIngredientGrammInline(admin.TabularInline):
    model = DishIngredientGramm
    extra = 1
    autocomplete_fields = ["dish_ingredient"]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    inlines = [DishIngredientGrammInline]


@admin.register(DishIngredient)
class DishIngredientAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(DishIngredientGramm)
class DishIngredientGrammAdmin(admin.ModelAdmin):
    list_display = ("dish", "dish_ingredient", "gramm")
    list_filter = ("dish",)
