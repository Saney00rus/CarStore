from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from store.models import ad_car
from store.serializers import CarstoreSerializer


class CarstoreAPIView(APIView):
    def get(self, request):
        c = ad_car.objects.all()
        return Response({'posts': CarstoreSerializer(c, many=True).data})



# class CarstoreViewSet(ModelViewSet):
#     queryset = ad_car.objects.all()
#     serializer_class = CarstoreSerializer
