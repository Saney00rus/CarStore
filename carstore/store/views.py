from rest_framework import generics
from rest_framework.permissions import *
from store.permissions import IsOwner
from store.serializers import *


class CarstoreAPIList(generics.ListCreateAPIView):
    queryset = ad_car.objects.all()
    serializer_class = CarstoreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CarstoreAPIUpdateAndDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ad_car.objects.all()
    serializer_class = CarstoreSerializer
    permission_classes = (IsOwner | IsAdminUser,)


class CarstoreAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = ad_car.objects.all()
    serializer_class = CarstoreSerializer
    permission_classes = (IsOwner | IsAdminUser,)
