from rest_framework import serializers
from .models import Things, Suplier

class ThingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Things
        fields = ['name', 'description', 'price', 'exist', 'suplier']
