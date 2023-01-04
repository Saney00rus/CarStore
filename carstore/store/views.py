from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from store.models import ad_car
from store.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from store.serializers import CarstoreSerializer


class CarstoreAPIList(generics.ListCreateAPIView):
    queryset = ad_car.objects.all()
    serializer_class = CarstoreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CarstoreAPIUpdate(generics.UpdateAPIView):
    queryset = ad_car.objects.all()
    serializer_class = CarstoreSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CarstoreAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = ad_car.objects.all()
    serializer_class = CarstoreSerializer
    permission_classes = (IsAdminOrReadOnly,)
