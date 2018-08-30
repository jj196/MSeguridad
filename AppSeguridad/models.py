# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

# Create your models here.
class Seguridad(models.Model):
    Usuario = models.CharField(max_length=255)
    Huella = models.CharField(max_length=255)
    Email = models.CharField(max_length=500)

