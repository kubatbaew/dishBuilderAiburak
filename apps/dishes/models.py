from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Dish(models.Model):
    image = models.ImageField(
        upload_to="dishes/",
        verbose_name="Картинка"
    )
    title = models.CharField(
        verbose_name="Название",
        max_length=120,
    )
    description = models.TextField(
        max_length=750,
        verbose_name="Описание",
    )
    quote = models.CharField(
        max_length=100,
        verbose_name="Цитата",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class DishIngredient(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Название",
    )
    image = models.ImageField(
        upload_to="dish_ingredients/",
    )
    slug = models.SlugField(
        unique=True,
        null=True,
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Ингредиент Блюда"
        verbose_name_plural = "Ингредиенты Блюда"


class DishIngredientGramm(models.Model):
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE,
        verbose_name="Блюдо",
        related_name="ingredients_gramms",
    )
    dish_ingredient = models.ForeignKey(
        DishIngredient, on_delete=models.CASCADE,
        verbose_name="Ингредиент Блюда"
    )
    gramm = models.PositiveSmallIntegerField(
        verbose_name="Грамм",
        help_text="Граммовка на 300 грамм блюдо"
    )

    def __str__(self):
        return f"{self.dish_ingredient} — {self.gramm} г"
    
    class Meta:
        verbose_name = "Ингредиент Блюда Грамм"
        verbose_name_plural = "Ингредиенты Блюда Граммы"
        unique_together = ("dish", "dish_ingredient")


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="my_favorite",
        verbose_name="Пользователь",
    )
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE,
        verbose_name="Блюдо"
    )

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Избранный"
        verbose_name_plural = "Избранные"


class FavoriteItems(models.Model):
    favorite = models.ForeignKey(
        Favorite, on_delete=models.CASCADE,
        related_name="favorites_items",
        verbose_name="Избранное",
    )
    title = models.CharField(   
        max_length=120,
        verbose_name="Название",
    )
    gramm = models.PositiveSmallIntegerField(
        verbose_name="Грамм",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Элемент избранных"
        verbose_name_plural = "Элементы избранных"
