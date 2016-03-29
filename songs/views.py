from django.http import HttpResponse
from .models import Album


def albums(request):
    album_list = Album.objects.order_by('-pub_date')[:5]
    output = ', '.join([a.album_name for a in album_list])
    return HttpResponse(output)
