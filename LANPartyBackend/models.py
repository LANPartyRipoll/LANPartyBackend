# -*- coding: utf-8 -*-

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Inscripcions(models.Model):
    nom = models.TextField()
    cognom = models.TextField()
    email = models.TextField()
    telefon = models.TextField()
    categoria = models.TextField()
    equip = models.TextField()
    nick = models.TextField()
    dni = models.TextField()
    naixement = models.TextField()
    poblacio = models.TextField()
    major = models.TextField()
    pagat = models.TextField()
    present = models.BooleanField(db_column='Present')  # Field name made lowercase.


    class Meta:
        db_table = 'inscripcions'


class Tiquets(models.Model):
    qr_id = models.TextField(null=True, unique=True, max_length=255)
    scanned = models.BooleanField()
    inscripcio=models.ForeignKey('Inscripcions',on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = 'tiquets'
