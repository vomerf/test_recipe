from django.contrib import admin

from .models import Product, Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'times_used')
    search_fields = ['name']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    inlines = [RecipeIngredientInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)
