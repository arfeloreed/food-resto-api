from rest_framework import serializers

from .models import Food


# serializer models below
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"
