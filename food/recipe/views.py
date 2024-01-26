from django.shortcuts import render, get_object_or_404
from recipe.models import RecipeIngredient, Recipe, Product
from django.db import transaction
from django.db.models import Q


def add_product_to_recipe(request, recipe_id, product_id, weight):
    '''
        Просходит присваивание конкретного продукта к конкретному рецепту
        происходит это путем передачи id рецепта и продукта в url.
        Также передается вес продукта.
    '''
    recipe_ingredient = RecipeIngredient.objects.filter(
        recipe=recipe_id,
        product=product_id
    )
    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
        'recipe': recipe,
        'weight': weight
    }
    if recipe_ingredient:
        concrete_recipe_ingredient = recipe_ingredient[0]
        concrete_recipe_ingredient.weight_in_grams = weight
        concrete_recipe_ingredient.save()
        return render(
            request,
            template_name='update_weight_in_exists_recipe.html',
            context=context
        )
    RecipeIngredient.objects.create(
        product=product,
        recipe=recipe,
        weight_in_grams=weight
    )
    return render(
        request, template_name='add_product_in_recipe.html', context=context
    )


@transaction.atomic
def cook_recipe(request, recipe_id):
    '''
        Уведичивается счяетчик каждого продукта
        связанному с конкретным рецептом.
    '''
    recipe = get_object_or_404(Recipe, id=recipe_id)
    for ingredient in recipe.products.all():
        ingredient.times_used += 1
        ingredient.save()


def show_recipes_without_product(request, product_id):
    '''
        Возвращаются все рецепты в табличном виде
        которые не входят в конкретный продукт либо входят,
        но количество меньше 10 грамм.
    '''
    product = get_object_or_404(Product, id=product_id)
    recipes = product.ingredients.exclude(
        Q(
            recipeingredient__product=product_id,
            recipeingredient__weight_in_grams__gte=10
        )
    )
    return render(
        request,
        template_name='show_recipes_without_product.html',
        context={'recipes': recipes}
    )
