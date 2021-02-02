import os
import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from io import BytesIO
from places.models import Place, Picture


class Command(BaseCommand):
    help = 'Add place from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('place_url', help='ссылка на json места', type=str)

    def handle(self, *args, **options):
        place_response = requests.get(options['place_url'])
        place_response.raise_for_status()
        place = place_response.json()
        obj, created = Place.objects.get_or_create(
            title=place['title'], short_description=place['description_short'],
            long_description=place['description_long'],
            lon=place['coordinates']['lng'], lat=place['coordinates']['lat']
        )
        if created:
            for idx, img_url in enumerate(place['imgs']):
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                filename = os.path.basename(img_url)
                picture = Picture.objects.create(place=obj, position=idx+1)
                picture.image.save(
                    filename,
                    ContentFile(BytesIO(img_response.content).getvalue()),
                    save=False
                )
                picture.save()


