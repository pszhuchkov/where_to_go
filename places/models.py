from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description_short = models.TextField(verbose_name='Краткое описание', blank=True)
    description_long = HTMLField(verbose_name='Полное описание', blank=True)
    lon = models.FloatField(verbose_name='Долгота', null=True, blank=True)
    lat = models.FloatField(verbose_name='Широта', null=True, blank=True)

    def __str__(self):
        return self.title


class Picture(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    position = models.IntegerField(verbose_name='Позиция')
    place = models.ForeignKey('Place', on_delete=models.CASCADE,
                              verbose_name='Место', related_name='pictures')

    def __str__(self):
        return f'{self.position} {self.place.title}'

    class Meta(object):
        ordering = ['position']
