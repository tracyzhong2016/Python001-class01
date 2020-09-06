# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Smzdm1(models.Model):
    comments = models.CharField(max_length=1024, blank=True, null=True)
    sentiments = models.FloatField(blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    comment_time = models.CharField(max_length=45, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'smzdm1'
