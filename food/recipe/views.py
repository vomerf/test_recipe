from django.shortcuts import render, get_object_or_404
from recipe.models import RecipeIngredient, Recipe, Product
from django.db import transaction
from django.db.models import Q, F


@transaction.atomic
def add_product_to_recipe(request, recipe_id, product_id, weight):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    try:
        recipe_ingredient = RecipeIngredient.objects.select_for_update().get(
            recipe=recipe,
            product=product,
        )
        recipe_ingredient.weight_in_grams = weight
        recipe_ingredient.save()

        context = {
            'product': product,
            'recipe': recipe,
            'weight': weight
        }
        return render(
            request,
            template_name='update_weight_in_exists_recipe.html',
            context=context
        )

    except RecipeIngredient.DoesNotExist:
        recipe_ingredient = RecipeIngredient.objects.create(
            recipe=recipe,
            product=product,
            weight_in_grams=weight
        )

        context = {
            'product': product,
            'recipe': recipe,
            'weight': weight
        }
        return render(
            request,
            template_name='add_product_in_recipe.html',
            context=context
        )


@transaction.atomic
def cook_recipe(request, recipe_id):
    '''
        Уведичивается счяетчик каждого продукта
        связанному с конкретным рецептом.
    '''
    recipe = get_object_or_404(Recipe, id=recipe_id)
    for ingredient in recipe.products.all():
        ingredient.times_used = F('times_used') + 1
        ingredient.save()


def show_recipes_without_product(request, product_id):
    '''
        Возвращаются все рецепты в табличном виде
        которые не входят в конкретный продукт либо входят,
        но количество меньше 10 грамм.
    '''
    product = get_object_or_404(Product, id=product_id)
    recipes = Recipe.objects.filter(
        Q(
            ~Q(products__recipeingredient__product=product) |
            Q(
                products__recipeingredient__product=product,
                products__recipeingredient__weight_in_grams__lt=10
            )
        )
    ).distinct()
    return render(
        request,
        template_name='show_recipes_without_product.html',
        context={'recipes': recipes}
    )
