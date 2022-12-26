from rest_framework.viewsets import ModelViewSet

from store.models import ad_car
from store.serializers import CarstoreSerializer


class CarstoreViewSet(ModelViewSet):
    queryset = ad_car.objects.all()
    serializer_class = CarstoreSerializer
