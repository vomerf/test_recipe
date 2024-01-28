from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    times_used = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField(
        Product,
        through='RecipeIngredient',
        related_name='recipe'
    )

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight_in_grams = models.IntegerField()

    def __str__(self):
        return f'{self.product.name} ({self.weight_in_grams}g)'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'product'],
                name='unique_recipe_product'
            ),
        ]
