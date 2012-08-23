from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Corporation(models.Model):
    name = models.CharField(max_length=100)
    # add any other details here - address etc


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    corporation = models.ForeignKey('account.Corporation')


def create_profile(sender, instance=None, **kwargs):
    if instance is None:
        return None
    profile, created = Profile.objects.get_or_create(user=instance)
post_save.connect(create_profile, sender=User)
