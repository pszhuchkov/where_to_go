from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from places.models import Place


def format_place_for_display_on_map(place):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.lon, place.lat]
        },
        'properties': {
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': reverse('place-detail', args=[place.id])
        }
    }


def index(request):
    places = Place.objects.all()

    places_feature_collection = {
        'type': 'FeatureCollection',
        'features': [format_place_for_display_on_map(place) for place in places]
    }

    context = {
        'places': places_feature_collection
    }

    return render(request, 'index.html', context)


def serialize_place_for_api(place):
    return {
        'title': place.title,
        'imgs': [picture.image.url for picture in
                 place.pictures.order_by('position')],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat
        }
    }


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    serialized_place_for_api = serialize_place_for_api(place)
    return JsonResponse(serialized_place_for_api,
                        json_dumps_params={'ensure_ascii': False, 'indent': 4})
