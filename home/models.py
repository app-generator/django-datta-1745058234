# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Cards(models.Model):

    #__Cards_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    typeline = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    human_readable_type = models.CharField(max_length=255, null=True, blank=True)
    frame_type = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    race = models.CharField(max_length=255, null=True, blank=True)
    atk = models.IntegerField(null=True, blank=True)
    def = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    attribute = models.CharField(max_length=255, null=True, blank=True)
    archetype = models.CharField(max_length=255, null=True, blank=True)
    linkval = models.IntegerField(null=True, blank=True)
    linkmarkers = models.CharField(max_length=255, null=True, blank=True)
    cardset = models.CharField(max_length=255, null=True, blank=True)
    image_url_small = models.CharField(max_length=255, null=True, blank=True)
    ygoprodeck_url = models.CharField(max_length=255, null=True, blank=True)

    #__Cards_FIELDS__END

    class Meta:
        verbose_name        = _("Cards")
        verbose_name_plural = _("Cards")



#__MODELS__END
