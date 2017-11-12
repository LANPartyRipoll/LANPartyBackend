from rest_framework import serializers
from .models import Inscripcions, Tiquets

class InscripcioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcions
        fields = ('nom', 'cognom', 'categoria', 'equip', 'nick', 'major', 'pagat')

class TiquetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiquets
        fields = ('qr_id' ,'scanned', 'inscripcio')
