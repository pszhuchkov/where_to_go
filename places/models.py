from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование', unique=True)
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    long_description = HTMLField(verbose_name='Полное описание', blank=True)
    lon = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Picture(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    position = models.IntegerField(verbose_name='Позиция', blank=True, null=True, default=0)
    place = models.ForeignKey('Place', on_delete=models.CASCADE,
                              verbose_name='Место', related_name='pictures')

    def __str__(self):
        return f'{self.position} {self.place.title}'

    class Meta(object):
        ordering = ['position']
