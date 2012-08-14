from django.db import models


class RawProduct(models.Model):
    """ Example: Coffee Beans """
    name = models.CharField(max_length=255)
    shelf_life = models.PositiveSmallIntegerField(default=0)


class RegularUnit(models.Model):
    """ Example: Kgs, std_unit = lbs, std_qty = 0.45 """
    name = models.CharField(max_length=150)
    abbr = models.CharField(max_length=7)
    std_qty =  models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    std_unit = models.ForeignKey('self', related_name='standard_name')