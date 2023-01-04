from .models import ad_car
from rest_framework import serializers


class CarstoreSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ad_car
        fields = '__all__'
