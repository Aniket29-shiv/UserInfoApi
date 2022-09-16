from rest_framework import serializers

from .models import InputTable
class InputTableserializer(serializers.ModelSerializer):
    class Meta:
        model = InputTable
        fields='__all__'
