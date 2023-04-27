from rest_framework import serializers
from .models import events


class eventserializer(serializers.ModelSerializer):
    class Meta:
        model = events
        fields = '__all__'


