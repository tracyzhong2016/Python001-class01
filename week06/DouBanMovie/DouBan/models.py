from django.db import models


class DoubanMovie(models.Model):
    id = models.AutoField(primary_key=True)

    rate = models.BigIntegerField(blank=True, null=True)
    short = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'douban_movie'
