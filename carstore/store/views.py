from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from store.models import ad_car
from store.serializers import CarstoreSerializer


class CarstoreAPIView(APIView):
    def get(self, request):
        c = ad_car.objects.all()
        return Response({'posts': CarstoreSerializer(c, many=True).data})

    def post(self, request):
        serializer = CarstoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = ad_car.objects.create(
            mark=request.data['mark'],
            mod=request.data['mod'],
            year=request.data['year'],
            millage=request.data['millage'],
            owners=request.data['owners'],
            price=request.data['price'],
            description=request.data['description'],
            user=request.data['user']
        )

        return Response({'post': CarstoreSerializer(post_new).data})

# class CarstoreViewSet(ModelViewSet):
#     queryset = ad_car.objects.all()
#     serializer_class = CarstoreSerializer
