from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description_short = models.CharField(max_length=300, verbose_name='Краткое описание', blank=True)
    description_long = models.TextField(verbose_name='Полное описание', blank=True)
    lon = models.FloatField(verbose_name='Долгота', null=True, blank=True)
    lat = models.FloatField(verbose_name='Широта', null=True, blank=True)

    def __str__(self):
        return self.title
