# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cihai(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    words = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    yin = models.CharField(max_length=255, blank=True, null=True)
    yun = models.CharField(max_length=255, blank=True, null=True)
    key1 = models.CharField(max_length=255, blank=True, null=True)
    key2 = models.CharField(max_length=255, blank=True, null=True)
    key3 = models.CharField(max_length=255, blank=True, null=True)
    key4 = models.CharField(max_length=255, blank=True, null=True)
    key5 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cihai'


class Words(models.Model):
    word = models.CharField(max_length=255)
    pron = models.CharField(max_length=255, blank=True, null=True)
    ch = models.CharField(max_length=255, blank=True, null=True)
    key1 = models.CharField(max_length=255, blank=True, null=True)
    key2 = models.CharField(max_length=255, blank=True, null=True)
    key3 = models.CharField(max_length=255, blank=True, null=True)
    key4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'words'
