from rest_framework import serializers

from .models import Reserve

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = ('id', 'name', 'email', 'phone', 'date', 'time', 'guests', 'message')