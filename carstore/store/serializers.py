from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer
from store.models import ad_car


class CarstoreSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.username')
    class Meta:
        model = ad_car
        fields = '__all__'
