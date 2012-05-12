from django.contrib import admin
from recipe.models import Recipe, RecipeItem

class RecipeAdmin(admin.ModelAdmin):
    pass

class RecipeItemAdmin(admin.ModelAdmin):
	pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeItem, RecipeItemAdmin)
