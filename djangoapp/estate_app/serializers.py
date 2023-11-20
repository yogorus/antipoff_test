import re

# from django.contrib.gis.geos import Point
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import CadastralRequest

# from django.contrib.gis.ge
CADASTRAL_NUMBER_REGEX = r"^(?:[0-9]{1,2}:){2}[0-9]{6,7}:[0-9]{1,3}$"


class CadastralInputSerializer(serializers.Serializer):
    cadastral_number = serializers.CharField(required=True)
    latitude = serializers.DecimalField(decimal_places=6, max_digits=9, required=True)
    longitude = serializers.DecimalField(decimal_places=6, max_digits=9, required=True)
    # status = serializers.BooleanField(required=False)
    # date = serializers.DateTimeField(required=False)

    class Meta:
        model = CadastralRequest
        # fields = ["cadastral_number", "latitude", "longitude"]
        fields = "__all__"

    def validate(self, data):
        cadastral_number = data.get("cadastral_number")
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if not re.match(CADASTRAL_NUMBER_REGEX, cadastral_number):
            raise ValidationError("invalid cadastral number")

        try:
            # Convert latitude and longitude to decimal degrees
            latitude = float(latitude)
            longitude = float(longitude)

            # Check if latitude and longitude are within valid range
            if latitude < -90 or latitude > 90:
                raise ValidationError("Invalid latitude")
            if longitude < -180 or longitude > 180:
                raise ValidationError("Invalid longitude")

        except ValueError:
            raise ValidationError("Invalid latitude or longitude")

        return data

    def create(self, data):
        pass


class CadastralResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastralRequest
        fields = "__all__"
