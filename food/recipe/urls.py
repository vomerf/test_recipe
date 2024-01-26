from recipe.views import add_product_to_recipe, cook_recipe, show_recipes_without_product
from django.urls import path

urlpatterns = [
    path(
        'add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/',
        add_product_to_recipe,
        name='add_recipe'
    ),
    path(
        'cook_recipe/<int:recipe_id>/', cook_recipe, name='cook_recipe'
    ),
    path(
        'show_recipes_without_product/<int:product_id>/',
        show_recipes_without_product,
        name='show_recipes'
        )
]
