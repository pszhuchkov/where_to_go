from django.shortcuts import render
from places.models import Place


def format_place(place):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.lon, place.lat]
        },
        'properties': {
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': 'static/places/moscow_legends.json'
        }
    }


def index(request):
    places = Place.objects.all()

    places_to_geojson = {
        'type': 'FeatureCollection',
        'features': [format_place(place) for place in places]
    }

    context = {
        'places': places_to_geojson
    }

    return render(request, 'index.html', context)
