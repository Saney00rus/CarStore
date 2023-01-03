from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer
from store.models import ad_car
from rest_framework import serializers


# class CarstoreSerializer(ModelSerializer):
#     user = ReadOnlyField(source='user.username')
#     class Meta:
#         model = ad_car
#         fields = '__all__'

class CarstoreSerializer(serializers.Serializer):
    mark = serializers.CharField(max_length=255)
    mod = serializers.CharField(max_length=255)
    year = serializers.IntegerField()
    millage = serializers.IntegerField()
    owners = serializers.IntegerField()
    images = serializers.ImageField(null=True, blank=True)
    price = serializers.IntegerField()
    description = serializers.CharField()
    user = serializers.IntegerField()
