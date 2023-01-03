from rest_framework import viewsets

from store.models import ad_car
from store.serializers import CarstoreSerializer

class CarstoreViewSet(viewsets.ModelViewSet):
    queryset = ad_car.objects.all()
    serializer_class = CarstoreSerializer
