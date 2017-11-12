from rest_framework import serializers
from .models import Inscripcions, Tiquets

class InscripcioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcions
        fields = ('nom', 'cognom')

class TiquetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiquets
        fields = ('qr_id' ,'scanned', 'inscripcio')
