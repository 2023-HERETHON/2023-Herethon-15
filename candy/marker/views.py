from django.shortcuts import render

from .models import Marker

# Create your views here.
def marker_view(request):
    if request.method=='GET':
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        filtered_markers = Marker.objects.filter(
            latitude__range=(latitude - 0.005, latitude + 0.005),
            longitude__range=(longitude - 0.005, longitude + 0.005)
        )
        return render(request, './marker/marker.html', { "markers" : filtered_markers })
