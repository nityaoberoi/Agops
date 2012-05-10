from django.db import models

class Recipe(models.Model):
    """ Example: Guacamole """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    shelf_life = models.PositiveSmallIntegerField(default=0)

class RecipeItem(models.Model):
    recipe = models.ForeignKey('recipe.Recipe') # TODO: Possibly convert this into an M2M relationship
    raw_product = models.ForeignKey('product.RawProduct')
    quantity = models.PositiveSmallIntegerField(default=0, help_text='Number of this unit. e.g.: 18oz -> 18')
    unit = models.ForeignKey('product.RegularUnit', help_text='Unit of this product. 18oz -> oz')
